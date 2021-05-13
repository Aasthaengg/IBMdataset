import math
a,b,c = map(int,input().split())
print(float(0.5*a*b*math.sin(c*math.pi/180)))
print(float(a+b+math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c*math.pi/180))))
print(float(b*math.sin(c*math.pi/180)))


