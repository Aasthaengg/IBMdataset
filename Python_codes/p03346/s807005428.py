#!/usr/bin/env python3
#AGC24 B

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
p = [I() for _ in range(n)]
inde = [0]*n
for i in range(n):
    inde[p[i]-1] = i
cnt = 1
ans = 0
for i in range(1,n):
    if inde[i-1] < inde[i]:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 1
ans = max(ans,cnt)
ans = n - ans
print(ans)
