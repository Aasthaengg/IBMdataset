import sys
input = sys.stdin.readline
from collections import *

def bfs():
    q = deque([K-1])
    dist = [-1]*N
    dist[K-1] = 0
    
    while q:
        v = q.popleft()
        
        for nv, w in G[v]:
            if dist[nv]==-1:
                dist[nv] = dist[v]+w
                q.append(nv)
    
    return dist

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, c))
    G[b-1].append((a-1, c))

Q, K = map(int, input().split())
dist = bfs()

for _ in range(Q):
    x, y = map(int, input().split())
    print(dist[x-1]+dist[y-1])