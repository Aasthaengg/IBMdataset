import sys
input = sys.stdin.readline
from collections import *

def bfs(s):
    q = deque([s])
    dist = [-1]*N
    dist[s] = 0
    
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

d1 = bfs(0)
d2 = bfs(N-1)
c = 0

for i in range(N):
    if d1[i]<=d2[i]:
        c += 1

if c>N-c:
    print('Fennec')
else:
    print('Snuke')