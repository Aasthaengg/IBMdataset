# -*- coding: utf-8 -*-
#E - Hopscotch Addict
import sys 
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, M = map(int, readline().split())
graph = [[[] for _ in range(3)] for _ in range(N+1)]
for i in range(M):
    x,y = map(int,readline().split())
    graph[x][0].append((y,1))
    graph[x][1].append((y,2))
    graph[x][2].append((y,0))
S,G = map(int,readline().split())
dist = [[-1]*3 for _ in range(N+1)]
dist[S][0] = 0
root = (S,0)

q = deque([root])
def bfs(q):
    while q:
        x,t = q.popleft()
        for nx,nt in graph[x][t]:
            if dist[nx][nt] != -1:
                continue
            dist[nx][nt] = dist[x][t] + 1
            q.append((nx,nt))
            
bfs(q)
if dist[G][0] == -1:
    print(-1)
else:
    print(dist[G][0] // 3)