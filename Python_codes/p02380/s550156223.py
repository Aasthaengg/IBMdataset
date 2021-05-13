import math
a, b, d = map(float, input().split())
h = b * math.sin(d*math.pi/180)
s = a * h / 2
l = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(d*math.pi/180)) + a + b
print(s)
print(l)
print(h)
