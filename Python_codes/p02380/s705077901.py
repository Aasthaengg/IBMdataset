import math as m
a, b, c = map(float, input().split())
c = m.radians(c)
S = a * b * m.sin(c) * (1/2)
l = m.sqrt(a**2 + b**2 - 2 * a * b * m.cos(c))
L = a + b + l
h = b * m.sin(c)
print("%.5f\n%.5f\n%.5f" % (S, L, h))