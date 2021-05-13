#!/usr/bin/env python3
#ABC116 D

import sys
import math
import bisect
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
mod = 10**9 + 7

n,k = map(int,input().split())
td = [list(map(int,input().split())) for _ in range(n)]
td.sort(key = itemgetter(1),reverse = True)
f = [0]*n
ans = 0
kind = 0
x = []
for i in range(k):
    t,d = td[i]
    ans += d
    if not f[t-1]:
        kind += 1
    else:
        x.append(d)
    f[t-1] += 1
ans += kind**2
x.sort()
x = deque(x)
y = ans
for i in range(k,n):
    t,d = td[i]
    if not x:
        break
    if f[t-1]:
        continue
    y += d - x.popleft() + 2*kind + 1
    f[t-1] = 1
    kind += 1
    ans = max(ans,y)
print(ans)
