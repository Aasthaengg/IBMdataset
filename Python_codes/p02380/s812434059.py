import math
a,b,C = map(float,input().split())
S = (1/2)*a*b*math.sin(math.radians(C))
L = (a**2+b**2-2*a*b*math.cos(math.radians(C)))**(1/2)+a+b
h = b*math.sin(math.radians(C))
print(f"{S:.8f}")
print(f"{L:.8f}")
print(f"{h:.8f}")
