from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
a = inpl()
res = 0
for i in range(k+1):
    pick = i; back = k-i
    for j in range(pick+1):
        l = j; r = pick-j
        q = deque(a)
        # print(l,r)
        now = []
        while q and l > 0:
            now.append(q.popleft())
            l -= 1
        while q and r > 0:
            now.append(q.pop())
            r -= 1
        now.sort(); ln = len(now)
        ans = sum(now)
        res = max(res, ans)
        for i in range(back):
            if i >= ln: continue
            ans -= now[i]
            res = max(res, ans)
print(res)