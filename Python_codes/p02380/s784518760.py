from math import radians, cos, sin, sqrt

a, b, c = map(float, input().split())

c = radians(c)
h = b * sin(c)
s = a * h * 1 / 2

d = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(c))
l = a + b + d

print(s)
print(l)
print(h)
