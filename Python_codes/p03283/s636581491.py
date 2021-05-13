n,m,q=map(int,input().split())
LR=[list(map(int,input().split())) for _ in range(m)]
PQ=[list(map(int,input().split())) for _ in range(q)]

DP=[[0 for _ in range(n+1)] for _ in range(n+1)]
for l,r in LR:
    DP[l][r] +=1

for i in range(1,n+1):
    for j in range(1,n+1):
        DP[i][j]=DP[i-1][j]+DP[i][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        DP[i][j]=DP[i][j-1]+DP[i][j]
        
for p,q in PQ:
    print(DP[q][q]-DP[q][p-1]-DP[p-1][q]+DP[p-1][p-1])