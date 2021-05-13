import math
a,b,c = map(float,input().split())
S = 0.5*a*b*math.sin(c*math.pi/180)
L = a+b+(a*a+b*b-2*a*b*math.cos(c*math.pi/180))**0.5
print(S,L,b*math.sin(c*math.pi/180))