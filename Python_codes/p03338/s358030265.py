#! /usr/bin/env python3

from fractions import gcd
# from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

N = int(input())
S = input()

c = Counter(S)

mcount = len(c)

mct = 0
for i in range(N):
    ta = Counter(S[:i])
    tb = Counter(S[i:])
    
    ct = 0
    for st in ta:
        if tb[st]:
           ct += 1
           
    mct = max(mct, ct)
print(mct)
