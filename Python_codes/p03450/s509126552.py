from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
g = [[] for _ in range(n)]
for i in range(m):
    l,r,d = inpl()
    g[l-1].append((r-1,d))
    g[r-1].append((l-1,-d))
seen = [False] * n
dist = [0] * n
for i in range(n):
    if seen[i]:
        continue
    q = deque([i])
    while q:
        now = q.popleft()
        seen[i] = True
        for v,d in g[now]:
            if seen[v]:
                if dist[v] != d + dist[now] :
                    print('No')
                    quit()
            else:
                dist[v] = dist[now] + d
                seen[v] = True
                q.append(v)
print('Yes')
