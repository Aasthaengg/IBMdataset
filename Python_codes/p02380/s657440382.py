from __future__ import division, print_function
from sys import stdin
from math import radians, sin, cos, sqrt
a, b, degree = (float(s) for s in stdin.readline().split())
h = b * sin(radians(degree))
s = a * h / 2.0
L = sqrt(a**2 + b**2 - 2.0*a*b*cos(radians(degree))) + a + b
print('{:.4f}\n{:.4f}\n{:.4f}'.format(s, L, h))