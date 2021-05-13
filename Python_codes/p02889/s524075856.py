import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m,l=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        if(c>l): continue
        a-=1; b-=1
        E[a].append((b,c))
        E[b].append((a,c))

    # 各頂点を始点としたDijkstra
    A=[None]*n
    for s in range(n):
        dist=[(INF,INF)]*n
        dist[s]=(0,0)
        visited=[0]*n
        for _ in range(n-1):
            v=min((dist[v],v) for v in range(n) if(not visited[v]))[1]
            visited[v]=1
            for nv,w in E[v]:
                a,b=dist[v]
                if(b+w<=l): na,nb=a,b+w
                else: na,nb=a+1,w
                if(dist[nv]>(na,nb)):
                    dist[nv]=(na,nb)
        A[s]=dist

    for _ in range(int(input())):
        s,t=map(int,input().split())
        s-=1; t-=1
        print(A[s][t][0] if(A[s][t][0]!=INF) else -1)
resolve()