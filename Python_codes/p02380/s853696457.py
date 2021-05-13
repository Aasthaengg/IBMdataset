from math import sin, cos, radians, sqrt

a, b, C = map(float, input().split())
C = radians(C)
S = a * b * sin(C) * 0.5
h = 2.0 * S / a
c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(C))
L = a + b + c
print("{:.10f}".format(S))
print("{:.10f}".format(L))
print("{:.10f}".format(h))

