import math as m
a,b,c=map(int,input().split())
sinc=m.sin(m.radians(c))
cosc=m.cos(m.radians(c))
h=b*sinc
d=(h**2+(a-b*cosc)**2)**(1/2)
print('{:.10f}'.format((1/2)*a*b*sinc))
print('{:.10f}'.format(b+a+d))
print('{:.10f}'.format(h))
