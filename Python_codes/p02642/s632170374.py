from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

a.sort()

count = Counter(a)

b = [1 for i in range((max(a) + 1))]

for aa in a:
    for j in range(2*aa,len(b), aa):
        b[j] = 0

c = 0
for d in count.items():
    if d[1] == 1 and b[d[0]] == 1: c += 1

print(c)