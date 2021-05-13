n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[0] + [float('inf')]*(n-1)
for i in range(n):
    for j in range(max(0,i-k),i):
        dp[i]=min(dp[i],dp[j]+abs(h[i]-h[j]))
print(dp[-1])