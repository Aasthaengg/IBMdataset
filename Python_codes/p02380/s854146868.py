import math
a, b, C = map(int, input().split())

C_rad = C * math.pi / 180.0

h = b * math.sin(C_rad)
S = a * h / 2.0
c = math.sqrt(math.pow(h, 2) + math.pow(a - b * math.cos(C_rad), 2))
L = a + b + c

print(S)
print(L)
print(h)