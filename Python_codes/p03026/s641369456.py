import sys
input = sys.stdin.readline
from collections import *

def bfs():
    q = deque([0])
    dist = [-1]*N
    dist[0] = 0
    
    while q:
        v = q.popleft()
        
        for nv in G[v]:
            if dist[nv]==-1:
                dist[nv] = dist[v]+1
                q.append(nv)
    
    return dist

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

c = list(map(int, input().split()))
c.sort(reverse=True)
dist = bfs()
idist = [(i, dist[i]) for i in range(N)]
idist.sort(key=lambda t: t[1])
ans = [-1]*N

for i in range(N):
    ans[idist[i][0]] = c[i]

print(sum(c[1:]))
print(*ans)