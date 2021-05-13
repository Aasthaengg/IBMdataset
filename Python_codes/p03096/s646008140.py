n = int(input())
iro = [-1 for i in range(2*(10**5)+1)]
dp = [1 for i in range(n+1)]
mod = 10**9 + 7
for i in range(1,n+1):
    dp[i] = dp[i-1]
    now = int(input())
    if iro[now] != -1 and iro[now] != i-1:
        dp[i] += dp[iro[now]]
    iro[now] = i
    dp[i] %= mod
print(dp[n])