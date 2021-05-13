import math
n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[math.inf for i in range(n)]
dp[0]=0
for i in range(1,n):
    for j in range(1,k+1):
        if i-j<0:
            continue
        dp[i]=min(dp[i-j]+abs(h[i]-h[i-j]),dp[i])
print(dp[n-1])