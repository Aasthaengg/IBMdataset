#! /usr/bin/env python3

from fractions import gcd
# from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

import copy

N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(M)]

road = [ [] for i in range(N) ]

for ab in AB:
    road[ab[0]-1] += [ab[1]-1]
    road[ab[1]-1] += [ab[0]-1]

rets = [0 for i in range(N)]
visited = [0] * N
visited[0] = 1

D = deque([0])

while D:
    v = D.popleft()
    for i in road[v]:
        if visited[i]: continue
        visited[i] = 1
        rets[i] = v
        D.append(i)

print("Yes")
for i in rets[1:]:
    print(i+1)