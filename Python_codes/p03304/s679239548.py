#!/usr/bin/env python3
#SoundHound C

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
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n,m,d = LI()
ans = 0
if d == 0:
    for i in range(m-1):
        ans += n/pow(n,2)
    print(ans)
else:
    for i in range(m-1):
        ans += (2*(n-d))/pow(n,2)
    print(ans)
