from itertools import permutations
N,M,R=map(int, input().split())
G=[[float("INF")]*N for _ in range(N)]
r=list(map(int, input().split()))
for i in range(M):
    a,b,c=map(int, input().split())
    G[a-1][b-1]=c
    G[b-1][a-1]=c

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
#print(G)
for i in range(N):
    G[i][i] = 0 #自身のところに行くコストは０
warshall_floyd(G)


#print(G)

ans=float("INf")
for t in permutations(r):
    sub=0
    #print(t)
    for i in range(R):
        if i==0:
            now=t[i]
        sub+=G[now-1][t[i]-1]
        now=t[i]
        #print(now)
    ans=min(ans, sub)
print(ans)