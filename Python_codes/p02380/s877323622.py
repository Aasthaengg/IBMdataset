import math

a,b,C = map(float,input().split())

h = b * math.sin(math.pi*C/180)
S = a * h /2
L = a + b +(a**2 + b**2 - 2*a*b*math.cos(math.pi*C/180))**(0.5)

print(S,L,h)