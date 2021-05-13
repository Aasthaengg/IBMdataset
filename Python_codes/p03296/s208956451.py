#!/usr/bin/env python3
#AGC26 A

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
a = LI()
cnt = 1
ans = 0
for i in range(1,n):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        ans += cnt // 2
        cnt = 1
ans += cnt // 2
print(ans)
