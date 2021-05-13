import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import deque
def resolve():
    n,m=map(int,input().split())
    N=3*n
    E=[[] for _ in range(N)]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[3*u].append(3*v+1)
        E[3*u+1].append(3*v+2)
        E[3*u+2].append(3*v)

    s,t=map(int,input().split())
    s-=1; t-=1
    S=3*s; T=3*t
    dist=[INF]*N
    dist[S]=0
    Q=deque([S])
    while(Q):
        v=Q.popleft()
        for nv in E[v]:
            if(dist[nv]!=INF): continue
            dist[nv]=dist[v]+1
            Q.append(nv)

    print(dist[T]//3 if(dist[T]!=INF) else -1)
resolve()