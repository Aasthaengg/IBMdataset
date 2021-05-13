import math

a, b, C = [float(_) for _ in input().split()]

S = 0.5 * a * b * math.sin(math.radians(C))
c = math.sqrt(pow(a,2) + pow(b,2) - 2 * a * b * math.cos(math.radians(C)))
L = a + b + c
h = S / a * 2
print(S)
print(L)
print(h)