from itertools import permutations

n,m,r=list(map(int,input().split()))
rlst=list(map(int,input().split()))
inf=10**20

d=[[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=list(map(int,input().split()))
    d[a][b]=c
    d[b][a]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
ans=inf
for comb in permutations(rlst,r):
    i=0
    tans=0

    while i+1<r:
        tans+=d[comb[i]][comb[i+1]]
        i+=1
    
    ans=min(ans,tans)

print(ans)