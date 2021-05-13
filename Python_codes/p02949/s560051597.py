import sys
input = sys.stdin.readline
from collections import *

def bfs(s, g):
    q = deque([s])
    dist = [-1]*N
    dist[s] = 0
    
    while q:
        v = q.popleft()
        
        for nv in g[v]:
            if dist[nv]==-1:
                dist[nv] = dist[v]+1
                q.append(nv)
    
    return dist

def bellman_ford():
    dist = [10**18]*N
    dist[0] = 0
    
    for i in range(N):
        for s, t, w in edges:
            if d1[s]==-1 or d2[t]==-1:
                continue
            
            if dist[t]>dist[s]+w:
                dist[t] = dist[s]+w
                
                if i==N-1:
                    print(-1)
                    exit()
        
    return -dist[N-1]
    
N, M, P = map(int, input().split())
G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    G[A-1].append(B-1)
    rG[B-1].append(A-1)
    edges.append((A-1, B-1, -(C-P)))

d1 = bfs(0, G)
d2 = bfs(N-1, rG)
print(max(0, bellman_ford()))