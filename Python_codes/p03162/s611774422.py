N=int(input())
dp=[[0]*N for i in range(3)]
for i in range(N):
    a,b,c=list(map(int,input().split()))
    if(i==0):
        dp[0][i]=a
        dp[1][i]=b
        dp[2][i]=c
    else:
        dp[0][i]=max(dp[1][i-1],dp[2][i-1])+a
        dp[1][i]=max(dp[0][i-1],dp[2][i-1])+b
        dp[2][i]=max(dp[0][i-1],dp[1][i-1])+c
print(max(dp[i][N-1] for i in range(3)))