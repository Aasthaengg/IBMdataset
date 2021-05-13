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
X = []
Y = []
for _ in range(n):
    x,y = LI()
    xy.append([x,y])
    X.append(x)
    Y.append(y)
X.sort(reverse = True)
Y.sort(reverse = True)
ans = inf
for i in range(n):
    uy = Y[i]
    for j in range(i+1,n):
        dy = Y[j]
        for k in range(n):
            rx = X[k]
            for l in range(k+1,n):
                lx = X[l]
                cnt = 0
                for x,y in xy:
                    if lx <= x <= rx and dy <= y <= uy:
                        cnt += 1
                if cnt >= K:
                    S = (uy - dy)*(rx - lx)
                    ans = min(ans,S)
print(ans)
