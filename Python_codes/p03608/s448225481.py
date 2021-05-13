import itertools
N,M,R=map(int, input().split())
r=list(map(int, input().split()))
G = [[float("inf")]*N for i in range(N)] 
for i in range(M):
    a,b,c=map(int, input().split())
    G[a-1][b-1]=c
    G[b-1][a-1]=c

def warshall_floyd(G):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j],G[i][k] + G[k][j])
    return G
G=warshall_floyd(G)
ans=10**8
for L in itertools.permutations(r):
    L=list(L)
    sub=0
    for i in range(1,R):
        s=L[i-1]
        t=L[i]
        sub+=G[s-1][t-1]
    ans=min(ans, sub)
print(ans)