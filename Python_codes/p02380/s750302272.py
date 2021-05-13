a,b,C=map(float,input().split())
import math
r=C*(math.pi)/180
S=1/2*a*b*(math.sin(r))
c=(a**2+b**2-2*a*b*(math.cos(r)))**(1/2)
L=a+b+c
h=b*(math.sin(r))
print(S)
print(L)
print(h)
