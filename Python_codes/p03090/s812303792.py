#!/usr/bin/env python3
#AGC32 B

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
m = n*(n-1)//2
ans = []
for i in range(n):
    for j in range(i+1,n):
        ans.append((i+1,j+1))
lst = []
if n % 2:
    for i in range(n//2):
        lst.append((i+1,n-i-1))
        m -= 1
else:
    for i in range(n//2):
        lst.append((i+1,n-i))
        m -= 1
for i,j in lst:
    ans.remove((i,j))
print(m)
for i,j in ans:
    print(i,j)
