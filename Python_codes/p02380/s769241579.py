from math import sin, cos, sqrt, radians
a, b, C = map(int, input().split())
C = radians(C)
S = .5 * a * b * sin(C)
h = b * sin(C)
c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(C))
L = a + b + c
print(S)
print(L)
print(h)