import sys
input = sys.stdin.readline
from collections import *

def bfs():
    q = deque([0])
    dist = [-1]*N
    dist[0] = 0
    
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
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))

dist = bfs()
ans = [0]*N

for i in range(N):
    if dist[i]%2==0:
        ans[i] = 1

for ans_i in ans:
    print(ans_i)