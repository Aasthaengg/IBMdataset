import math
lst=input().split()
lst=list(map(lambda i:int(i),lst))
a,b,C=lst[0],lst[1],lst[2]
S=(1/2)*a*b*math.sin(math.radians(C))
h=(2/a)*S
c=(a**2+b**2-2*a*b*math.cos(math.radians(C)))**(1/2)
L=a+b+c
print(S)
print(L)
print(h)

