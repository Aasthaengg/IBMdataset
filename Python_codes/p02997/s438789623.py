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

n, k = LI()
if k > (n - 1) * (n - 2) // 2:
    print(-1)
else:
    print((n - 1) * (n - 2) // 2 - k  + (n - 1))
    edges = []
    for i in range(2, n+1):
        edges.append((1, i))
    cnt = 0
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if cnt == (n - 1) * (n - 2) // 2 - k:
                break
            edges.append((i, j))
            cnt += 1
        else:
            continue
        break
    for u, v in edges:
        print(u, v)