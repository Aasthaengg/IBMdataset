a,b,h,m=map(int,input().split())

kk=h*30-5.5*m
if kk <0:
    kk+=360

import math
c= math.cos(math.radians(kk))

print((a*a+b*b-2*a*b*c)**0.5)