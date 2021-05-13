#!/usr/bin/env python3
#AGC19 B

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

a = input()
n = len(a)
c = list(Counter(a).items())
ans = n*(n-1)//2 + 1
for i,j in c:
    ans -= j*(j-1)//2
print(ans)
