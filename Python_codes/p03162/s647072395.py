n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*3 for _ in range(n)]
dp[0]=l[0]
for i in range(n-1):
    for j in range(3):
        dp[i+1][j]=max(dp[i][(j+1)%3]+l[i+1][j],dp[i][(j+2)%3]+l[i+1][j])
print(max(dp[n-1]))