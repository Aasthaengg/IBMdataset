#!/usr/bin/env python3
#ABC60 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

n,W = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(n)]
mw = wv[0][0]
w = [[] for _ in range(4)]
for i,j in wv:
    w[i-mw].append(j)
for i in range(4):
    w[i].sort(reverse = True)
    w[i] = list(accumulate(w[i]))
w = [[0] + w[i] for i in range(4)]
a,b,c,d = len(w[0]),len(w[1]),len(w[2]),len(w[3])
ans = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            for l in range(d):
                if i*mw + j*(mw+1) + k*(mw+2) + l*(mw+3) <= W:
                    ans = max(ans,w[0][i]+w[1][j]+w[2][k]+w[3][l])
print(ans)
