#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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
ans = 0
info = [[] for _ in range(n)]
for i in range(n):
    a = I()
    for _ in range(a):
        x, y = LI()
        info[i].append((x-1, y))

for i in range(1, 1 << n):
    ret = 0
    for j in range(n):
        if i >> j & 1:
            ret += 1
            for x, y in info[j]:
                if y == 0 and i >> x & 1:
                    break
                elif y == 1 and not i >> x & 1: 
                    break
            else:
                continue
            break
    else:
        ans = max(ans, ret)
print(ans)
