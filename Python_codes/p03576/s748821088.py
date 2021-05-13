#!/usr/bin/env python3
#ABC75 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))


n,K = LI()
xy = []
for _ in range(n):
    x,y = LI()
    xy.append((x,y))
ans = inf
for _ , uy in xy:
    for _ , dy in xy:
        if uy < dy:
            continue
        for rx , _ in xy:
            for lx , _ in xy:
                if rx < lx:
                    continue
                cnt = 0
                for x,y in xy:
                    if lx <= x <= rx and dy <= y <= uy:
                        cnt += 1
                if cnt >= K:
                    ans = min(ans,(rx - lx)*(uy - dy))
print(ans)
