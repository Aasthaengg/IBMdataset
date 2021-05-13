import sys
sys.setrecursionlimit(10**6)
def dfs(v,p,d):
    dist[v]=d
    for nv,nd in G[v]:
        if nv==p:
            continue
        dfs(nv,v,d+nd)

N=int(input())
G=[[] for i in range(N)]
dist=[-1]*N
for i in range(N-1):
    a,b,c=map(int,input().split())
    G[a-1].append([b-1,c])
    G[b-1].append([a-1,c])
Q,K=map(int,input().split())
dfs(K-1,-1,0)
for i in range(Q):
    x,y=map(lambda x:int(x)-1,input().split())
    print(dist[x]+dist[y])