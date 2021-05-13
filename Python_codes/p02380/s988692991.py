import math
a,b,cdeg= map(float, input().strip().split())
crad = cdeg*math.pi/180
print(a*b/2*math.sin(crad))
print(a+b+math.sqrt(a**2 + b**2 -2*a*b*math.cos(crad)))
print(b*math.sin(crad))