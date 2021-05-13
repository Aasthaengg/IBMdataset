from math import sin, cos, radians, sqrt
a, b, C = [float(i) for i in input().split(" ")]
S = a * b * sin(radians(C)) / 2
L = a + b + sqrt( a**2 + b**2 - 2*a*b*( cos(radians(C)) ) )
h = 2 * S / a

print(S,L,h,sep = "\n")