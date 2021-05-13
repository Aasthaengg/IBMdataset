import math
a,b,h,m=[int(x) for x in input().split()]
theta=30*h-m*(11/2)
l=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(theta)))
print(l)