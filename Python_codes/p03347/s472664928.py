#!/usr/bin/env python3
#AGC24 C

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
a = [I() for _ in range(n)]
if a[0] != 0:
    print(-1)
    quit()
for i in range(1,n):
    if a[i] - a[i-1] > 1:
        print(-1)
        quit()
ans = 0
for i in range(1,n):
    if a[i] == a[i-1] and a[i] > 0:
        ans += a[i]
    elif a[i] == a[i-1] + 1:
        ans += 1
    elif a[i] < a[i-1]:
        ans += a[i]
print(ans)
