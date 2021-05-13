import math
a,b,c=map(float,input().split())
if c == 90:
    S=(a*b/2)
    L=(math.sqrt(a**2+b**2)+a+b)
    h=(2*S/a)
else:
    S=(math.sin(math.radians(c))*a*b/2)
    L=(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c))))
    h=(2*S/a)
print(S)
print(L)
print(h)
