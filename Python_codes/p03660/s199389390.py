# -*- coding: utf-8 -*-
import sys
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
f_dist = [-1]*(N+1)
s_dist = [-1]*(N+1)
G = [[] for _ in range(N+1) ]
for _ in range(N-1):
    x, y = map(int,readline().split())
    G[x].append(y)
    G[y].append(x)
    
def dfs(q,dist):       
    while q:
        x = q.popleft()
        for nx in G[x]:
            if dist[nx] != -1:
                continue
            dist[nx] = dist[x] + 1
            q.append(nx)

q = deque([1])
f_dist[1] = 0
dfs(q,f_dist)
q = deque([N])
s_dist[N] = 0
dfs(q,s_dist)
f_cnt = 0
s_cnt = 0
for i in range(1,N+1):
    if f_dist[i] <= s_dist[i]:
        f_cnt += 1
    else:
        s_cnt += 1
if f_cnt > s_cnt:
    print('Fennec')
else:
    print('Snuke')
