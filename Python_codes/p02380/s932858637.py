import math
values=input().split()
a=float(values[0])
b=float(values[1])
C=int(values[2])
sinC=math.sin(math.radians(C))
cosC=math.cos(math.radians(C))
S=1/2*a*b*sinC
c=pow(pow(a,2)+pow(b,2)-2*a*b*cosC,0.5)
L=a+b+c
h=2*S/a
print(S,L,h)
