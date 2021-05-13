from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
a = inpl()
res = 0
for ope in range(k+1):
    for pick in range(ope+1):
        if pick > n: continue
        back = ope - pick
        for lp in range(pick+1):
            rp = pick - lp
            # print(ope,back,lp,rp)
            q = []
            for i in range(lp):
                q.append(a[i])
            for i in range(rp):
                q.append(a[-i-1])
            q.sort()
            ans = sum(q)
            res = max(res,ans)
            for i in range(back):
                if i >= pick: break
                ans -= q[i]
                res = max(res,ans)
print(res)