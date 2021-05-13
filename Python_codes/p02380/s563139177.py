import math
a,b,C = map(int, input().split())
c = math.radians(C)
h = b * math.sin(c)
s = a * h / 2
a2 = a - b * math.cos(c)
c2 = math.sqrt(h**2 + a2**2)
l = a + b + c2

print("%f" % s)
print("%f" % l)
print("%f" % h)