from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n,m,q = inpl()
abc = [inpl() for _ in range(q)]
q = deque()
q.append([1])
res = 0
while q:
    now = q.popleft()
    if len(now) == n+1:
        # print(now)
        ans = 0
        for i,x in enumerate(abc):
            a,b,c,d = x
            if now[b] - now[a] == c:
                ans += d
        res = max(ans, res)
        continue
    for i in range(now[-1], m+1):
        q.append(now + [i])
print(res)
