#!/usr/bin/env python3
#AGC14 B

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

n,m = LI()
cnt = [0]*n
for _ in range(m):
    a,b = LI()
    cnt[a-1] += 1
    cnt[b-1] += 1
for i in range(n):
    if cnt[i] % 2:
        print('NO')
        quit()
print('YES')
