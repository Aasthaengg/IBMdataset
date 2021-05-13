from collections import deque

import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,M=map(int,input().split())
g=[[] for _ in range(N)]
gr=[[] for _ in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    gr[v-1].append(u-1)
S,T=map(int,input().split())


f = [[-1,-1,-1] for _ in range(N)]
f[S-1][0] = 0
q=deque([[S-1,0]])

while q:
    d,s = q.popleft()
    s += 1
    for sd in g[d]:
        if f[sd][s%3]==-1:
            f[sd][s%3] = s//3
            q.append([sd,s])


print(f[T-1][0])
