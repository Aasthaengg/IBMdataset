from math import *
a, b, h, m = [int(_) for _ in input().split()]
print((a**2 + b**2 - 2*a*b * cos(radians(h*330 + m*5.5))) ** 0.5)