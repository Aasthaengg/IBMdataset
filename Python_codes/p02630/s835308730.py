from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque

n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

m = sum([k*v for (k,v) in d.items()])

q = int(input())

for i in range(q):
    b, c = list(map(int, input().split()))

    if b in d:
        m += (c - b)*d[b]

        if c not in d:
            d[c] = d[b]
        else:
            d[c] += d[b]

        d[b] = 0

    print(m)


