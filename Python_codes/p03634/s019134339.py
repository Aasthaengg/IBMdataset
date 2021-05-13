from collections import deque

N=int(input())

E={i:{} for i in range(1,N+1)}

for _ in range(N-1):
    a,b,c=map(int,input().split())
    E[a][b]=c
    E[b][a]=c

Q,K=map(int,input().split())
inf=float("inf")
Dist=[inf]*(N+1)
Dist[K]=0
X=deque([K])

while X:
    u=X.popleft()
    for v in E[u]:
        if Dist[v]==inf:
            X.append(v)
            Dist[v]=Dist[u]+E[u][v]

T=[0]*Q
for i in range(Q):
    x,y=map(int,input().split())
    T[i]=Dist[x]+Dist[y]

print("\n".join(map(str,T)))