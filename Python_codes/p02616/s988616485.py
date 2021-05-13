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
a = LI()
a.sort(key = lambda x:abs(x), reverse = True)
ans = 1
p = 0
m = 0
plus = []
minus = []
use = []
f = 0
for i in range(n):
    if a[i] >= 0:
        p += 1
        if i < k:
            plus.append(a[i])
            use.append(a[i])
            ans *= a[i]
            ans %= mod
    else:
        m += 1
        if i < k:
            minus.append(a[i])
            f ^= 1
            use.append(a[i])
            ans *= -a[i]
            ans %= mod
if f:
    ans = -ans
if ans < 0:
    if k == n:
        print(ans % mod)
    elif p == 0:
        a.sort(key = lambda x:abs(x))
        ans = 1
        for i in range(k):
            ans *= -a[i]
            ans %= mod
        if k % 2:
            ans = -ans
        print(ans % mod)
    else:
        for i in range(k, n):
            if a[i] < 0:
                break
        else:
            ans = -ans
            ans *= pow(-minus[-1], mod-2, mod)
            ans *= max(a[k:])
            print(ans % mod)
            quit()
        if plus:
            ans = -ans
            ans *= pow(plus[-1], mod-2, mod)
            ans %= mod
            ans *= pow(-minus[-1], mod-2, mod)
            ans %= mod
            ans1 = plus[-1] * max(a[k:])
            ans2 = minus[-1] * min(a[k:])
            print(max(ans1, ans2) * ans % mod)
        else:
            ans = -ans
            ans *= pow(-minus[-1], mod-2, mod)
            ans %= mod
            ans *= max(a[k:])
            print(ans % mod)
else:
    print(ans)
