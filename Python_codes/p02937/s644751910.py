#!/usr/bin/env python3
#ABC138 E

import sys
import math
import bisect
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

s = input()
t = input()
n = len(s)
m = len(t)
f = [False]*26
f2 = [False]*26
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    f[alpha.index(s[i])] = True
for i in range(m):
    f2[alpha.index(t[i])] = True
for i in range(26):
    if not f[i] and f2[i]:
        print(-1)
        quit()
ans = 0
inde = s.index(t[0])
ans += inde+1
for i in range(1,m):
    s = s[inde+1:] + s[:inde+1]
    inde = s.index(t[i])
    ans += inde+1
print(ans)
