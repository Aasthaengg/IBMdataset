import math
a,b,c = map(float,raw_input().split(' '))
H = b*math.sin(math.radians(c))
S = a*H/2
A = math.sqrt((b*b)-(H*H))
d = math.sqrt((a**2)+(b**2)-2*a*b*math.cos(math.radians(c)));
L = a+b+d
print S
print L
print H