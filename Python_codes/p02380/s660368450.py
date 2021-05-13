import math
a,b,c = map(float,input().split())
c = math.radians(c)
print(a*b*math.sin(c)/2)
print(a+b+math.sqrt(a**2 + b**2 - 2*a*b*(math.cos(c))))
print(b * math.sin(c))