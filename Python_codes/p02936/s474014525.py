from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,q = inpl()
g = [[] for _ in range(n)]
c = [0] * n
for _ in range(n-1):
    a,b = inpl()
    a,b = a-1,b-1
    g[a].append(b)
    g[b].append(a)
for _ in range(q):
    x,y = inpl()
    c[x-1] += y
seen = [False] * n
seen[0] = True
q = deque()
q.append(0)
while q:
    now = q.popleft()
    for v in g[now]:
        if seen[v]: continue
        c[v] += c[now]
        seen[v] = True
        q.append(v)
print(*c)