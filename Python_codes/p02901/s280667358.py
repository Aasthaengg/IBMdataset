n,m = map(int,input().split())
dp = [[10**9]*(2**n+5) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    res = 0
    for x in c:
        res|=1<<(x-1)
    for j in range(2**n):
        ni = i+1
        nj = j|res
        dp[ni][j] = min(dp[ni][j],dp[i][j])
        dp[ni][nj] = min(dp[ni][nj],dp[i][j]+a)
ans = dp[m][2**n-1]
if ans == 10**9:ans = -1
print(ans)