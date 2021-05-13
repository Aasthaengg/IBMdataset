#!/usr/bin/env python3
#ABC81 D

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
a = LI()
M,m = max(a),min(a)
Mi,mi = a.index(M),a.index(m)
for i in range(n-1):
    if a[i] > a[i+1]:
        break
else:
    print(0)
    quit()
for i in range(n):
    if a[i] < 0:
        break
else:
    print(n-1)
    for i in range(n-1):
        print(i+1,i+2)
    quit()
for i in range(n):
    if a[i] > 0:
        break
else:
    print(n-1)
    for i in range(n-1)[::-1]:
        print(i+2,i+1)
    quit()
if abs(M) >= abs(m):
    print((n-1)*2)
    for i in range(n):
        if i == Mi:
            continue
        print(Mi+1,i+1)
    for i in range(n-1):
        print(i+1,i+2)
else:
    print((n-1)*2)
    for i in range(n):
        if i == mi:
            continue
        print(mi+1,i+1)
    for i in range(n-1)[::-1]:
        print(i+2,i+1)

