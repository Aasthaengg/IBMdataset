import sys
import math
(a, b, C) = [float(i) for i in sys.stdin.readline().split()]
C = C * 2 * math.pi / 360
S = a * b * math.sin(C) / 2
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
L = a + b + c
h = 2 * S / a
print(S)
print(L)
print(h)