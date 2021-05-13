import math
A, B, C = map(int, open(0).read().split())
S = 0.5 * A * B * math.sin(math.radians(C))
L = A + B + math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(math.radians(C))))
h = B * math.sin(math.radians(C))
print(S)
print(L)
print(h)
