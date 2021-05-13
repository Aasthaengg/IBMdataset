import math

a, b, c = map(int, input().split())
c = math.radians(c)
s = a * b * math.sin(c) / 2
l = (a ** 2 + b ** 2 - 2 * a * b * math.cos(c)) ** (1/2) + a + b
h = s / a * 2

print(s)
print(l)
print(h)
