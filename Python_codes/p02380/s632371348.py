from __future__ import division
import math

a, b, C = map(int, raw_input().split())
S = a * b * math.sin(math.radians(C)) / 2
c = math.sqrt((a**2 + b**2 -2*a*b*math.cos(math.radians(C))))
L = a + b + c
h = b * math.sin(math.radians(C))

for i in S, L, h:
    print "{:.5f}".format(i)