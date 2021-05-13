#!/usr/bin/env python3
#ABC45 D

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

h,w,n = map(int,input().split())
f = defaultdict(lambda : 0)
for _ in range(n):
    a,b = map(int,input().split())
    if a-2 >= 1 and b-2 >= 1:
        f[(a-2,b-2)] += 1
    if a-2 >= 1 and b-1 >= 1 and b+1 <= w:
        f[(a-2,b-1)] += 1
    if a-2 >= 1 and b+2 <= w:
        f[(a-2,b)] += 1
    if a-1 >= 1 and b-2 >= 1 and a+1 <= h:
        f[(a-1,b-2)] += 1
    if a-1 >= 1 and b-1 >= 1 and a+1 <= h and b+1 <= w:
        f[(a-1,b-1)] += 1
    if a-1 >= 1 and b+2 <= w and a+1 <= h:
        f[(a-1,b)] += 1
    if a+2 <= h and b-2 >= 1:
        f[(a,b-2)] += 1
    if a+2 <= h and b-1 >= 1 and b+1 <= w:
        f[(a,b-1)] += 1
    if a+2 <= h and b+2 <= w:
        f[(a,b)] += 1
ans = [0]*10
cnt = 0
for i in f.values():
    ans[i] += 1
    cnt += 1
ans[0] = (h-2)*(w-2) - cnt
for i in ans:
    print(i)
