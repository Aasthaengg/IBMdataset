#!/usr/bin/env python3
#ABC68 D

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
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

k = I()
n = 50
ans = [i for i in range(n)]
d,m = divmod(k,n)
for i in range(n):
    ans[i] += d
    if n - i <= m:
        ans[i] += 1
print(n)
print(*ans)
