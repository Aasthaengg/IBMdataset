import math
a, b, C = map(int, raw_input().split())
S = (a * b * math.sin(math.radians(C))) / 2
c = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(C)))
L = a + b + c
h = (S * 2) / a
print("%f" % (S, ))
print("%f" % (L, ))
print("%f" % (h, ))