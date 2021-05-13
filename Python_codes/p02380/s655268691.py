import math
a,b,C = map(int,raw_input().split())
C = C*(math.pi/180)
S = 0.5*a * b * math.sin(C)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
L = a + b + c
h = b * math.sin(C)

print S
print L
print h