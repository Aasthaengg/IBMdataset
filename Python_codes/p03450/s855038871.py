import sys
input = sys.stdin.readline
from collections import *

def bfs(s):
    visited[s] = True
    q = deque([s])
    
    while q:
        v = q.popleft()
        
        for nv, w in G[v]:
            if not visited[nv]:
                visited[nv] = True
                dist[nv] = dist[v]+w
                q.append(nv)
            else:
                if dist[nv]!=dist[v]+w:
                    return False
    
    return True

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    L, R, D = map(int, input().split())
    G[L-1].append((R-1, D))
    G[R-1].append((L-1, -D))

visited = [False]*N
dist = [0]*N
flag = True

for i in range(N):
    if not visited[i]:
        flag &= bfs(i)

if flag:
    print('Yes')
else:
    print('No')