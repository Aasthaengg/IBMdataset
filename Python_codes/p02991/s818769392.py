# -*- coding: utf-8 -*-
import sys
from queue import Queue
# 12:55~
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
uv = [list(map(int,input().split())) for _ in range(M)]
S,T = map(int,input().split())

S -= 1
T -= 1
#%%
adj_list = [[[] for _ in range(3)] for _ in range(N)]
for u,v in uv:
    for i in range(3):
        adj_list[u-1][i].append([v-1,(i+1)%3])


INF = 10**9+7
dist = [[INF]*3 for _ in range(N)]
dist[S][0] = 0

stack = Queue()
stack.put([S,0])
while not stack.empty():
    v,c = stack.get()
    nxt_v = adj_list[v][c]
    for nv,nc in nxt_v:
        if dist[nv][nc]==INF:
            dist[nv][nc] = dist[v][c] + 1
            stack.put([nv,nc])
            
            
if dist[T][0]==INF:
    ans = -1
else:
    ans = dist[T][0]//3
print(ans)
            
        
        
        
    



