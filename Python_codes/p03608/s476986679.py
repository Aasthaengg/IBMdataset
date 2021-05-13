import itertools
INF=10**30
N,M,R=map(int,input().split())
r=list(map(lambda x:int(x)-1,input().split()))

dist=[[INF]*N for i in range(N)]
for i in range(M):
    A,B,C=map(int,input().split())
    A,B=A-1,B-1
    dist[A][B]=C
    dist[B][A]=C
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
ans=INF
for x in itertools.permutations(r):
    res=0
    for i in range(len(x)-1):
        res+=dist[x[i]][x[i+1]]
    ans=min(ans,res)
print(ans)