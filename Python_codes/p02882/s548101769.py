#かつてAC

import math

def culc(t):
    return math.degrees(math.atan(t))

a,b,x=map(int,input().split())
V=a**2*b

if x>=V/2:
    T=2*((b/a)-(x/(a**3)))
    print(culc(T))
else:
    T=(a*(b**2))/(2*x)
    print(culc(T))

