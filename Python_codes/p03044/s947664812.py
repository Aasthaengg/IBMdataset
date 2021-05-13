from collections import deque
N=int(input())
E={i:{} for i in range(1,N+1)}

for _ in range(N-1):
    u,v,w=map(int,input().split())
    E[u][v]=w%2
    E[v][u]=w%2

inf=float("inf")
Dist=[inf]*(N+1)
Q=deque([1])
Dist[1]=0
while Q:
    u=Q.popleft()
    for v in E[u]:
        if Dist[v]==inf:
            Q.append(v)
            Dist[v]=Dist[u]^E[u][v]
print("\n".join(map(str,Dist[1:])))