import math

(a, b, C) = [int(i) for i in input().split()]

cs = math.radians(C)

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(cs))

h = b * math.sin(cs)
S = a * h / 2
L = a + b + c

[print(format(i, '6f')) for i in [S, L, h]]