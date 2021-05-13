n=int(input())
routes=list(map(int,input().split()))
dp=[float("inf") for i in range(n)]
dp[0]=0
for i in range(n):
    for j in range(i+1,i+3):
        if j<n:
            dp[j]=min(dp[j],dp[i]+abs(routes[i]-routes[j]))
print(dp[-1])