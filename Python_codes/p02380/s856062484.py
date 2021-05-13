
import math

a,b,c=map(int,input().split())

print(a*b*math.sin(math.radians(c))/2)

print((a**2+b**2-2*a*b*math.cos(math.radians(c)))**(1/2)+a+b)

print(a*b*math.sin(math.radians(c))/a)
