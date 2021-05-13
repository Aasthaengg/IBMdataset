from math import pi, cos
a, b, h, m = map(int, input().split())
print((a**2 + b**2 - 2*a*b*cos(2*pi*(m/60 - (60*h + m)/720)))**0.5)