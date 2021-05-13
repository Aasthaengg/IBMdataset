from math import sqrt, sin, cos, radians

a, b, cc = map(int, input().split())
cc = radians(cc)
sinc = sin(cc)
s = a * b * sinc / 2
c = sqrt(a * a + b * b - 2 * a * b * cos(cc))
h = b * sinc
print(s)
print(a + b + c)
print(h)