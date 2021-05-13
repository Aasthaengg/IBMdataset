# coding: utf-8
# Your code here!

import math
a, b, C = map(float,input().split())

S = (1/2)*a*b*math.sin(math.radians(C))
L = (a**2+b**2 - 2*a*b*math.cos(math.radians(C)))**(1/2) + a + b
h = 2*S/a

print(S,L,h, sep="\n")
