# coding: utf-8
# Your code here!

import math

a,b,C = map(int, input().split())
S = a * b * math.sin(math.radians(C)) /2
c2 = a*a + b*b - 2 * a * b * math.cos(math.radians(C))
c = math.sqrt(c2)
L = a + b + c
h = 2 * S / a

print(S)
print(L)
print(h)
