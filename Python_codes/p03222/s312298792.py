#!/usr/bin/env python3
#ABC113 D

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

h,w,K = map(int,input().split())
if w == 1:
    print(1)
    quit()
dp = [[0]*(w) for _ in range(h+1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        x,y,z = 0,0,0
        for k in range(2**(w-1)):
            b = [0]*(w-1)
            for l in range(w-1):
                if (k>>l) & 1:
                    if b[l-1] == 1:
                        break
                    b[l] = 1
            else:
                if j > 0 and j < w-1:
                    if b[j-1] == 1 and b[j] == 0:
                        x += 1
                    elif b[j-1] == 0 and b[j] == 0:
                        y += 1
                    elif b[j-1] == 0 and b[j] == 1:
                        z += 1
                elif j == 0:
                    if b[j] == 0:
                        y += 1
                    elif b[j] == 1:
                        z += 1
                elif j == w-1:
                    if b[j-1] == 0:
                        y += 1
                    elif b[j-1] == 1:
                        x += 1
        if j > 0:
            dp[i+1][j-1] += x*dp[i][j]
            dp[i+1][j-1] %= mod
        if j + 1 < w:
            dp[i+1][j+1] += z*dp[i][j]
            dp[i+1][j+1] %= mod
        dp[i+1][j] += y*dp[i][j]
        dp[i+1][j] %= mod
print(dp[-1][K-1])
