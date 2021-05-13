#!/usr/bin/env python3
#ARC100 C

import sys
import math
import bisect
import time
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
b = [a[i] - (i+1) for i in range(n)]
b.sort()
if n % 2:
    c = b[n//2]
else:
    c = (b[n//2]+b[n//2-1])//2
ans = 0
for i in range(n):
    ans += abs(a[i] -(c + i+1))
print(ans)
