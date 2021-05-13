import math

a, b, C = map(float, input().split())

C = math.radians(C)

S = 0.5 * a * b * math.sin(C)

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))

L = a + b + c

h = 2 * S / a

print("{0}\n{1}\n{2}".format(S, L, h))