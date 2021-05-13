import warnings
import urllib2

data = map(int, raw_input().split())

a = data[0]
b = data[1] 


d = int(a / b)
r = a % b
f = (1.000000 * a) / b

print "%s %s %.30f" % (d, r, f)