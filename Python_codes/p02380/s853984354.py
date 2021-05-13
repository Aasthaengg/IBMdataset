from math import radians, sin, cos

a, b, r = map(float, raw_input().split())
r = radians(r)
h = b * sin(r)
c = (a**2 + b**2 - 2*a*b*cos(r))**0.5
l = a + b + c
s = a * h / 2
print s
print l
print h