from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque

n = int(stdin.readline().rstrip())
a = [x for x in stdin.readline().rstrip().split()]

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

m = sum([v*(v-1) // 2 for v in list(d.values())])

for i in range(n):
    v = d[a[i]]
    print(m + 1 - v)


