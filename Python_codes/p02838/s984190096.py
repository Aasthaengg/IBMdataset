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
a = LI()
cnt = [0] * 61
for i in a:
    for j in range(61):
        if i >> j & 1:
            cnt[j] += 1

ans = 0
for i in range(61):
    ans += pow(2, i, mod) * ((n - cnt[i]) * cnt[i])
    ans %= mod
print(ans)