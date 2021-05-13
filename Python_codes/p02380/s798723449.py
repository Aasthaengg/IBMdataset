import math
a, b, C = map(int, input().split())
rad = math.radians(C)
S = (a * b * math.sin(rad)) / 2
L = a + b + (a * a + b * b - 2 * a * b * math.cos(rad)) ** 0.5
h = 2 * S / a
print("%.10f %.10f %.10f" %(S, L, h))

