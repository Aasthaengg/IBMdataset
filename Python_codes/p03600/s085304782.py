#!/usr/bin/env python3
#ABC74 D

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
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

n = I()
a = [LI() for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans += a[i][j]

for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if i == k or j == k:
                continue
            if a[i][j] > a[i][k] + a[k][j]:
                print(-1)
                quit()
            if a[i][j] == a[i][k] + a[k][j]:
                ans -= a[i][j]
                break
print(ans)