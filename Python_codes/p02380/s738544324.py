import math

a, b, c = [int(i) for i in input().split()]
s = 0.5 * a * b * math.sin(math.radians(c))
l = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(c)))
h = 2 * s / a
print(s)
print(l)
print(h)