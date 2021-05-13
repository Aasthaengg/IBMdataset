from collections import deque
N,M = map(int,input().split())
list_edge = [[] for _ in range(N)]
deg = [0]*N
for _ in range(M):
    a,b = map(int,input().split())
    list_edge[a-1].append(b-1)
    deg[b-1] += 1
que = deque()
for v in range(N):
    if deg[v]==0:
        que.append(v)
dp = [0]*N
while que:
    v = que.popleft()
    list_nv = list_edge[v]
    for nv in list_nv:
        deg[nv] -= 1
        if deg[nv]==0:
            que.append(nv)
            dp[nv] = max(dp[v],dp[v]+1)
print(max(dp))