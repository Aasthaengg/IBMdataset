import math
a,b,C=map(float,raw_input().split())
rad=math.radians(C)
c=(a**2+b**2-2*a*b*math.cos(rad))**0.5
h=b*math.sin(rad)
print h*a/2
print a+b+c
print h