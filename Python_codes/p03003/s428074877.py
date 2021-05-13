n,m = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
mod = 10**9 + 7

dp = [[0 for j in range(m+1)] for i in range(n+1)]

sum_dp = [[0 for j in range(m+1)] for i in range(n+1)]

dp[0][0] = 1
for i,x in enumerate(S):
    for j,y in enumerate(T):
        if x == y:
            dp[i+1][j+1] = sum_dp[i][j]+1
            dp[i+1][j+1] %= mod
        else:
            dp[i+1][j+1] = 0
        sum_dp[i+1][j+1] = sum_dp[i][j+1]+sum_dp[i+1][j]-sum_dp[i][j]+dp[i+1][j+1]
        sum_dp[i+1][j+1] %= mod

ans = 0
for x in dp:
    ans += sum(x)
    ans %= mod

print(ans)