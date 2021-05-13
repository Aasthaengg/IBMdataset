#!/usr/bin/env python3
#C

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

n, c, k = LI()
t = [I() for _ in range(n)]
t.sort()
tmp = 0
cnt = 0
ans = 0
if c == 1:
    print(n)
    quit()
for i in range(n):
    if t[i] <= tmp:
        cnt += 1
        if cnt == c:
            cnt = 0
            ans += 1
            if i + 1 < n:
                tmp = t[i+1] + k
            else:
                ans += 1
                break
    else:
        tmp = t[i] + k
        cnt = 1
        ans += 1
print(ans)