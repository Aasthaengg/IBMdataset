import math

a, b, h, m = map(int, input().split())
ht = (h*60+m)/360*math.pi
mt = m/30*math.pi
hx = a * math.sin(ht)
hy = a * math.cos(ht)
mx = b * math.sin(mt)
my = b * math.cos(mt)
print(math.sqrt((hx-mx)**2+(hy-my)**2))