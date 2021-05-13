#!/usr/bin/env python
import math

a, b, C = input().split()
a = float(a)
b = float(b)
C = float(C)

c = math.sqrt(((a*a) + (b*b) - 2*a*b*math.cos(math.radians(C))))
L = a + b + c
S = a*b*math.sin(math.radians(C))/2
h = 2*S/a
print("%.5f\n%.5f\n%.5f" % (S, L, h))