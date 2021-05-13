import math
a, b, C = map(float, input().split())
C_rad = math.radians(C)
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C_rad))
S = a * b * math.sin(C_rad) / 2
L = a + b + c
h = b * math.sin(C_rad)
print("{0} {1} {2}".format(S, L, h))