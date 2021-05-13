#!/usr/bin/env python3
#ABC52 D

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

n,a,b = LI()
x = LI()
x.sort()
ans = 0
for i in range(1,n):
    ans += min((x[i]-x[i-1])*a,b)
print(ans)
