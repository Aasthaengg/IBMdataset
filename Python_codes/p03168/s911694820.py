#H,W=map(int,input().split())
N=int(input())
coin=list(map(float,input().split()))
p=10**9+7
ma=[]
dp=[[0]*(N+3) for i in range(N+3)]
dp[1][1]=coin[0]
dp[1][0]=1-coin[0]
for i in range(1,N):
     for j in range(0,N):
         if j==0:
             dp[i+1][0]=dp[i][0]*(1-coin[i])
         dp[i+1][j+1]=dp[i][j+1]*(1-coin[i])+dp[i][j]*coin[i]

print(sum(dp[N][N//2+1:N+1]))
