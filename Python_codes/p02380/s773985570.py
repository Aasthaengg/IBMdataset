import math
a, b, Cdeg = map(int, input().split())
Crad = math.radians(Cdeg)
c = (a**2+b**2-2*a*b*math.cos(Crad))**0.5
h = b*math.sin(Crad)
print(0.5*a*h)
print(a+b+c)
print(h)