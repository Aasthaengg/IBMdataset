N=int(input())
abc=[list(map(int,input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
for i in range(3):
    dp[0][i]=abc[0][i]
for i in range(1,N):
    for j in range(3):
        for k in range(3):
            if(j!=k):
                dp[i][j]=max(dp[i][j],dp[i-1][k]+abc[i][j])
print(max(dp[-1][2],max(dp[-1][0],dp[-1][1])))