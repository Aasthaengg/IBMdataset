from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
g = [[] for _ in range(n)]
for i in range(n-1):
    a,b = inpl()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
res = k
q = deque()
q.append(0)
fin = set()
fin.add(0)
while q:
    v = q.popleft()
    cnt = 1 if v == 0 else 2
    for nv in g[v]:
        if nv in fin:
            continue
        res *= k-cnt
        res %= mod
        cnt += 1
        fin.add(nv)
        q.append(nv)
print(res)