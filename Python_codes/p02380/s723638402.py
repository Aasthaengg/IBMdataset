import math
a,b,C = map(int,input().split())

S = (1/2) *a*b*math.sin(math.radians(C))
L = (a**2+b**2-2*a*b*math.cos(math.radians(C)))**(1/2)+a+b
h = 2*S/a
print(S)
print(L)
print(h)
