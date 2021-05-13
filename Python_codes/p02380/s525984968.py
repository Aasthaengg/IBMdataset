from math import *
a,b,C=map(int,input().split())
C2=radians(C)
S=float(a*b*sin(C2)/2)
L=float(a+b+((a**2+b**2-2*a*b*cos(C2))**(1/2)))
h=float(b*sin(C2))
print(S)
print(L)
print(h)