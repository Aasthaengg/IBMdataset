n=int(input())
H=[list(map(int,input().split())) for i in range(n)]
dp=[[0 for i in range(3)] for i in range(n)]
for i in range(3):
    dp[0][i]=H[0][i]
for i in range(n-1):
    for j in range(3):
        if j==0:
            dp[i+1][0]=max(dp[i][1]+H[i+1][0],dp[i][2]+H[i+1][0])
        if j==1:
            dp[i+1][1]=max(dp[i][0]+H[i+1][1],dp[i][2]+H[i+1][1])
        if j==2:
            dp[i+1][2]=max(dp[i][0]+H[i+1][2],dp[i][1]+H[i+1][2])
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))