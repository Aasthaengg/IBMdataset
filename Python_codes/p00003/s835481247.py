# coding: utf-8
# Here your code !

import sys
import math

r = sys.stdin.readlines()

n = [[int(i) for i in (j.split())] for j in r]

for i in range(1,n[0][0]+1):
    sq = []
    for a in n[i]:  #a is lengthes
        sq.append(a**2)
    if (sum(sq)-2*max(sq) == 0):
        print("YES")
    else:
        print("NO")