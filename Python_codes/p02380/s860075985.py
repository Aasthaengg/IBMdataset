import math
a,b,C=map(int,input().split())

S=(a*b*math.sin(C/180*math.pi))/2
L=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(C/180*math.pi))
h=2*S/a

print(S)
print(L)
print(h)
