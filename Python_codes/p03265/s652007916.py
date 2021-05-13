from cmath import exp
from math import pi
x1, y1, x2, y2 = map(int, input().split())
v = x2 - x1 + (y2-y1)*1j
v_ = v*exp(pi/2*1j)

x3 = round(x2+v_.real)
y3 = round(y2+v_.imag)

x4 = round(x1+v_.real)
y4 = round(y1+v_.imag)

print(x3, y3, x4, y4)