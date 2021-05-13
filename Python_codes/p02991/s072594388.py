# -*- coding: utf-8 -*-
#E - Hopscotch Addict
import sys 
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, M = map(int, readline().split())
graph = [[] for _ in range(3*N+1)]
for _ in range(M):
    x,y = map(int,readline().split())
    graph[x].append(y+N)
    graph[x+N].append(y+2*N)
    graph[x+2*N].append(y)
S,G = map(int,readline().split())
dist = [-1]*(N*3+1)
dist[S] = 0
root = S
q = deque([root])

def bfs(q):
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] != -1:
                continue
            dist[nx] = dist[x] + 1
            q.append(nx)
            
bfs(q)
if dist[G] == -1:
    print(-1)
else:
    print(dist[G] // 3)