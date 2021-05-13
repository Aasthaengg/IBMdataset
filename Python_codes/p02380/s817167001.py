import math
a,b,C=map(float,input().split())

S=0.5*a*b*math.sin(math.radians(C))

h=b*math.sin(math.radians(C))

c=math.sqrt(pow(a,2)+pow(b,2)-2*a*b*math.cos(math.radians(C)))

L=a+b+c



print(S)
print(L)
print(h)