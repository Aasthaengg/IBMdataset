import math
a,b,deg = map(float,input().split())
rad = math.radians(deg)
S = a * b * math.sin(rad) / 2
L = (a**2 + b**2 - 2*a*b*math.cos(rad))**0.5 + a + b
h = abs(b * math.sin(rad))
print(S)
print(L)
print(h)


