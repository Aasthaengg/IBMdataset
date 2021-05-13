from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
from decimal import Decimal
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,K = inpl()
a = [inpl() for _ in range(n)]
res = INF
a.sort(key=lambda x:x[0])
for j in range(n-1):
    for k in range(j+1,n):
        l = a[j][0]
        r = a[k][0]
        b = [a[j],a[k]]
        cnt = 2
        for _ in range(n):
            if _ == j or _ == k:
                continue
            if l < a[_][0] < r:
                cnt += 1
                b += [a[_]]
        if cnt < K: continue
        b.sort(key=lambda x:x[1])
        for _ in range(cnt-K+1):
            u = max(x[1] for x in b[_:_+K])
            d = min(x[1] for x in b[_:_+K])
            res = min(res, (r-l)*(u-d))
            # print(res)
print(res)
