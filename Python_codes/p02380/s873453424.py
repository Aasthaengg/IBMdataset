import math

a, b, C = [int(i) for i in input().split()]

S = 0.5 * a * b * math.sin(C * math.pi / 180)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C * math.pi / 180))
L = a + b + c
h = (2 * S) / a
print(S)
print(L)
print(h)