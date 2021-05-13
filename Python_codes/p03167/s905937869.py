h,w=map(int,input().split())
grid=[input() for _ in range(h)]
mod=10**9+7
dp=[0]*w
for  i in range(h):
    for j in range(w):
        if i==j==0:
            dp[j]=1
        elif grid[i][j]=='#':
            dp[j]=0
        elif j>0:
            dp[j]=dp[j]+dp[j-1]
print(dp[w-1]%mod)