from collections import deque

N,Q=map(int,input().split())
E={i:set() for i in range(1,N+1)}
for _ in range(N-1):
    a,b=map(int,input().split())
    E[a].add(b)
    E[b].add(a)

F=[0]*(N+1)
for _ in range(Q):
    p,x=map(int,input().split())
    F[p]+=x

T=[False]*(N+1)
T[1]=True
R=deque([1])

G=[0]*(N+1)
G[1]=F[1]
while R:
    u=R.popleft()
    for v in E[u]:
        if not T[v]:
            G[v]=G[u]+F[v]
            T[v]=True
            R.append(v)

for i in range(1,N+1):
    print(G[i])
