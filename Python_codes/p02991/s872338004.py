import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    dist = [-1]*(3*N)
    dist[serial[S][0]] = 0
    q = deque([serial[S][0]])
    
    while q:
        v = q.popleft()
        
        for nv in G[v]:
            if dist[nv]==-1:
                dist[nv] = dist[v]+1
                q.append(nv)
    
    return dist[serial[T][0]]

N, M = map(int, input().split())
serial = [[-1]*3 for _ in range(N)]
c = 0

for i in range(N):
    for j in range(3):
        serial[i][j] = c
        c += 1

G = [[] for _ in range(3*N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[serial[u][0]].append(serial[v][1])
    G[serial[u][1]].append(serial[v][2])
    G[serial[u][2]].append(serial[v][0])

S, T = map(int, input().split())
S -= 1
T -= 1
ans = bfs()

if ans==-1:
    print(-1)
else:
    print(ans//3)
