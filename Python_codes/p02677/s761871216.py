a,b,h,m=map(int,input().split())
x=abs(30*h-5.5*m)
y=min(x,360-x)
import math
rady=math.radians(y)
cosy=math.cos(rady)
c=(a**2+b**2-2*a*b*cosy)**0.5
print("{:.20}".format(c))