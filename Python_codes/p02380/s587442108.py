import math
a,b,C=map(float,input().split())
c1=math.sin(math.radians(C))
c2=math.cos(math.radians(C))
s=(1/2)*a*b*c1

d=(a*a+b*b-2*a*b*c2)**(1/2)
L=a+b+d

h=b*c1
print(s)
print(L)
print(h)
