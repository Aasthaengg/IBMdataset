import math
a, b, C = map(float, input().split())
cs = math.radians(C)
c = math.sqrt((a**2+b**2)-2*a*b*math.cos(cs))
h = b*math.sin(cs)
m = (a+b+c)*0.5
S = (m*(m-a)*(m-b)*(m-c))**0.5
L = a+b+c
print(f"{S:.8f}")
print(f"{L:.8f}")
print(f"{h:.8f}")
