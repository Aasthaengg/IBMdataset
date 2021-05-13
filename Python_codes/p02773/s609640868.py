from sys import stdin
import sys
import math
from functools import reduce
import itertools

n = int(stdin.readline().rstrip())

d = {}
for i in range(n):
    s = stdin.readline().rstrip()

    if s in d:
        d[s] += 1
    else:
        d[s] = 1

d = sorted(d.items(), key=lambda x:x[1], reverse=True)

m = d[0][1]
a = []
i = 0
for i in range(len(d)):
    if d[i][1] == m:
        a.append(d[i][0])
    else:
        break

a.sort()

for aa in a:
    print(aa)