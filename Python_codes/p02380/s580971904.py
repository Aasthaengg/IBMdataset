import math
a,b,C=map(float,input().split())
sinC=math.sin(math.radians(C))
cosC=math.cos(math.radians(C))
S=1/2*a*b*sinC
print(f'{S}')
c=math.sqrt(a*a+b*b-2*a*b*cosC)
print(f'{a+b+c}')
h=(2*S)/a
print(f'{h}')
