import math
a,b,h,m, = map(int,input().split())
al = 360*(60*h+m)/720
be = 360*m/60
x = (a**2 + b**2 - 2*a*b*math.cos(math.radians(al-be)))**(0.5)
print(x)