n=int(input())
happiness=[list(map(int,input().split())) for _ in range(n)]
dp=[[0 for _ in range(3)] for _ in range(n)]
dp[0][0],dp[0][1],dp[0][2]=happiness[0][0],happiness[0][1],happiness[0][2]
for i in range(1,n):
    for j in range(3):
        dp[i][j]=max(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3])+happiness[i][j]
print(max(dp[-1]))