H,W=map(int,input().split())
G=[list(str(input())) for _ in range(H)]
P=10**9+7

DP=[[0]*(W+1) for _ in range(H+1)]
DP[1][1]=1

for i in range(1,H+1):
    for j in range(1,W+1):
        if G[i-1][j-1]=='#':
            DP[i][j]=0
        else:
            DP[i][j]+=DP[i-1][j]+DP[i][j-1]
            DP[i][j]=DP[i][j]%P


print(DP[H][W])
