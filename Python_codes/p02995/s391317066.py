# -*- coding: utf-8 -*-
from math import gcd
a, b, c, d = map(int, input().split())

x = b - b//c - b//d + b//(int(c*d/gcd(c, d)))
y = (a-1) - (a-1)//c - (a-1)//d + (a-1)//(int(c*d/gcd(c, d)))
print(int(x-y))
