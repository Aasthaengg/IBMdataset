import math

a, b, Cd = map(int, input().split())
Cr = math.radians(Cd)

S = a * b * math.sin(Cr) * 0.5

c2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(Cr)

c = math.sqrt(c2)

L = a + b + c

h = 2 * S / a

print(S)
print(L)
print(h)