from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
edges = [inpl() for _ in range(m)]
res = 0
for ind in range(m):
    e = [[] for _ in range(n)]
    for i,(a,b) in enumerate(edges):
        if i == ind: continue
        e[a-1].append(b-1)
        e[b-1].append(a-1)
    seen = [False]*n
    cnt = 0
    for i in range(n):
        if seen[i]: continue    
        q = deque([])
        q.append(i)
        cnt += 1
        while q:
            now = q.popleft()
            if seen[now]: continue
            seen[now] = True
            for nx in e[now]:
                if seen[nx]: continue
                q.append(nx)
    if cnt != 1:
        res += 1
print(res)