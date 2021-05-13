import math
a, b, c = map(int, input().split())
r = math.radians(c)
S = math.sin(r) * a * b / 2
print(S)
d = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(r))
print(a + b + d)
h = math.sin(r) * b
print(h)