h,n = map(int,input().split())
data = []
ans = 0
M = -1
for _ in range(n):
    a,b = map(int,input().split())
    data.append((a,b))
    M = max(a,M)
dp = [float("inf") for _ in range(h+M)]
dp[0] = 0
for i,j in data:
    for k in range(h+M-1):
        if k+i <= h+M-1:
            dp[k+i] = min(dp[k]+j,dp[k+i])
print(min(dp[h:]))