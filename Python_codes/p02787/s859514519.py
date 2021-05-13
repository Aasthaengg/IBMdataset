H, N = map(int,input().split())
M = [list(map(int,input().split())) for k in range(N)]
dp = [10**10]*(10**5)
dp[0] = 0
for e in M:
    for k in range(e[0],10**5):
        dp[k] = min(dp[k],dp[k-e[0]]+e[1])
print(min(dp[H:]))
