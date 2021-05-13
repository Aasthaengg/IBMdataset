import math

a,b,cc=map(float,input().split())
sinc=math.sin(math.radians(cc))
cosc=math.cos(math.radians(cc))
c2=a*a+b*b-2*a*b*cosc

c=math.sqrt(c2)


S=(a*b*sinc)/2
L=a+b+c
H=b*sinc


print('{:.8f}'.format(S))
print('{:.8f}'.format(L))
print('{:.8f}'.format(H))
