import math

[a, b, C] = [float(x) for x in raw_input().split()]
C = math.radians(C)
c = math.sqrt(a ** 2.0 + b ** 2.0 - 2.0 * a * b * math.cos(C))
L = a + b + c
S = 0.5 * a * b * math.sin(C)
h = S / a * 2.0

print S, L, h