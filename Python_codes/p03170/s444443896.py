#!/usr/bin/env python3
#EDPC K

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

n,k = LI()
a = LI()
dp = [False]*(k+1)
for i in range(k+1):
    for j in a:
        if j <= i:
            if not dp[i-j]:
                dp[i] = True
if dp[-1]:
    print('First')
else:
    print('Second')