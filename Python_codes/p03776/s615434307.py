#!/usr/bin/env python3
#ABC57 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

n,a,b = map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse = True)
fact = [1]
for i in range(1,n+1):
    fact.append(fact[i-1]*(i))
def comb(n,r):
    return fact[n]// fact[r] //fact[n-r]
ans = sum(v[:a])/a
print(ans)
M,m = max(v[:a]),min(v[:a])
if M != m:
    c1,c2 = v[:a].count(m),v.count(m)
    print(comb(c2,c1))
else:
    ans = 0
    c = v.count(m)
    for i in range(a,b+1):
        if c >= i:
            ans += comb(c,i)
    print(ans)
