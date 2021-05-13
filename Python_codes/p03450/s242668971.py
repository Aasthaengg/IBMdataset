# -*- coding: utf-8 -*-
### 幅優先探索により矛盾を探す
import sys
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M = map(int,readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    L,R,D = map(int,readline().split())
    graph[L-1].append((R-1,D))
    graph[R-1].append((L-1,-D))

dist = [0]*N
done = [0]*N  
def bfs(i):
    q = deque([i])
    while q:
        x = q.popleft()
        for y,d in graph[x]:
            if done[y] == 0:
                done[y] = 1
                dist[y] = dist[x]+ d
                q.append(y)
            else:
                if dist[y] != dist[x]+d:
                    return 0
    return 1

for i in range(N):
    if done[i] == 0:
        done[i] = 1
        if bfs(i) == 0:
            print('No')
            sys.exit()
print('Yes')