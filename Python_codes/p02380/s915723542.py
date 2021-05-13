import math
a,b,C=map(int,input().split())
s=(a*b*math.sin(math.radians(C)))/2
c=(a**2+b**2-2*a*b*math.cos(math.radians(C)))**(1/2)
h=s*2/a
print(f'{s:4f}')
print(f'{a+b+c:4f}')
print(f'{h:4f}')

