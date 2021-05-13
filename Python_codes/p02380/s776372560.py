import math
a,b,c=map(float,input().split())
S=b*math.sin(math.radians(c))*a*1/2
x=math.sqrt(a**2 + b**2 -2*a*b*math.cos(math.radians(c)))
L=a+b+x
h=b*math.sin(math.radians(c))
print(format(S, '.8f'))
print(format(L, '.8f'))
print(format(h, '.8f'))
