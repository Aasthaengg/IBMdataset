# coding: utf-8
import math
a, b = input().split()
c = a + b
sq = math.sqrt(int(c))
d = math.floor(sq)
if math.pow(d, 2) == int(c):
    print("Yes")
else:
    print("No")