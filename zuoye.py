import urllib.request
import urllib.parse
# homewrok1: 定义一个函数,把参数写活
def spider_for_single(data):
data = urllib.parse.urlencode({'wd':'当'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)
# 把 路由和参数写活
def spider_for_single(data):
data = bytes(urllib.parse.urlencode({'pw':'123','acc':'456'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)