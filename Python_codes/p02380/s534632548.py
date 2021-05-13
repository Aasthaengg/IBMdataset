import math
a, b, C = map(int, input().split())
R = math.radians(C)
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(R))
L = a + b + c
S = a * b * math.sin(R) / 2
h = S * 2 / a
print(S)
print(L)
print(h)