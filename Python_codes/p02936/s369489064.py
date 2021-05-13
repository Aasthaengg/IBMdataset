import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.buffer.readline
def dfs(G,v,p):
    for nv in G[v]:
        if(nv==p):
            continue
        point[nv]+=point[v]
        dfs(G,nv,v)

N,Q=map(int,input().split())
G=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)
point=[0]*N
for i in range(Q):
    p,x=map(int,input().split())
    point[p-1]+=x
dfs(G,0,-1)
print(*point)
