n, m = map(int, input().split())
a = [None]*m
c = [0]*m
for i in range(m):
    a[i], b = map(int, input().split())
    ls = list(map(int,input().split()))
    for j in ls:
        c[i] |= 1<<(j-1)

dp = [[1e9]*(1<<n) for i in range(m+1)]
dp[0][0] = 0
for i in range(m):
    for S in range(1<<n):
        dp[i+1][S] = min(dp[i+1][S], dp[i][S])
        dp[i+1][S|c[i]] = min(dp[i+1][S|c[i]], dp[i][S]+a[i])
if dp[m][(1<<n)-1] < 1e9:
    print(dp[m][(1<<n)-1])
else:
    print(-1)