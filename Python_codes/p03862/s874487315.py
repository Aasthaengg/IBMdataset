import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7

n,x = map(int,input().split())
a = list(map(int,input().split()))
d = []
ans = 0
for i in range(n-1):
    d = a[i+1] + a[i]
    if d>=x:
        if a[i+1]>=d-x:
            a[i+1] = a[i+1] - (d-x)
            ans += d-x
        else:
            a[i+1] = 0
            a[i] -= d-x-a[i+1]
            ans += d-x-a[i+1]
    else:
        continue
print(ans)
