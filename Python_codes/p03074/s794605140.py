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
s = input()
C = []
x = s[0]
if x == '0':
    C.append(0)
cnt = 1
for i in range(1, n):
    if x != s[i]:
        C.append(cnt)
        cnt = 1
        x = s[i]
    else:
        cnt += 1
C.append(cnt)
if x != '1':
    C.append(0)
C = [0] + list(accumulate(C))
m = len(C)
if m < 2*k+1:
    print(C[-1])
else:
    ans = 0
    for i in range(2*k+1, m, 2):
        ans = max(ans, C[i] - C[i-(2*k+1)])
    print(ans)
