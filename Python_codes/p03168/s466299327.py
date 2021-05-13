N = int(input())
p = list(map(float, input().split()))

dp=[[0 for i in range(N+1)] for j in range(N+1)]
dp[0][1]=1-p[0]
dp[1][1]=p[0]
#print(dp)
for i in range(2,N+1):
    for j in range(N+1):
        dp[j][i]=dp[j][i-1]*(1-p[i-1])+dp[j-1][i-1]*p[i-1]
num=0
for i in range((N+1)//2):
    num+=dp[i][N]
print(1-num)