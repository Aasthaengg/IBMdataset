import math
a, b, h, m = map(int, input().split())

s = (60*h+m)/360*math.pi
l = m/30*math.pi
sx = a*math.sin(s)
sy = a*math.cos(s)
lx = b*math.sin(l)
ly = b*math.cos(l)
print(math.sqrt(((sx-lx)**2+(sy-ly)**2)))