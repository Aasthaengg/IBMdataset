import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m,L=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        u,v,w=map(int,input().split())
        if(w>L): continue
        u-=1; v-=1
        E[u].append((v,w))
        E[v].append((u,w))

    # 各始点からの Dijkstra
    # dist は (補給回数、補給してからの使用料)
    A=[None]*n
    for s in range(n):
        dist=[(INF,INF)]*n
        dist[s]=(0,0)
        used=[0]*n
        for _ in range(n-1):
            v=min((dist[v],v) for v in range(n) if(not used[v]))[1]
            used[v]=1
            c,l=dist[v]
            for nv,w in E[v]:
                if(l+w>L):
                    nd=(c+1,w)
                else:
                    nd=(c,l+w)
                dist[nv]=min(dist[nv],nd)
        A[s]=dist

    for _ in range(int(input())):
        s,t=map(int,input().split())
        s-=1; t-=1
        res=A[s][t][0]
        print(res if(res!=INF) else -1)
resolve()