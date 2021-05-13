import math
a,b,h,m=map(int,input().split())

A=30*h+0.5*m
B=6*m
point=abs(A-B)
C=math.cos(math.radians(min(point,360-point)))

print((a**2+b**2-2*a*b*C)**0.5)