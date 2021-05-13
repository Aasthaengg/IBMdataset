import math
a,b,c=map(int,input().split())
sinc=math.sin(math.radians(c))
cosc=math.cos(math.radians(c))
s=1/2*a*b*sinc
l=math.sqrt(a**2+b**2-2*a*b*cosc)+a+b
h=s*2/a
print(s)
print(l)
print(h)
