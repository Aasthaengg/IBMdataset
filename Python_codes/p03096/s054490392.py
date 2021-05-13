n = int(raw_input())
c = [int(raw_input()) for i in range(n)]
mod = 1000000007

dp = [0] * len(c)
last = [-1] * 200001
dp[0] = 1
last[c[0]] = 0
for i in range(1, len(c)):
    dp[i] = dp[i - 1]
    if last[c[i]] >= 0 and last[c[i]] < i - 1:
        dp[i] = (dp[i] + dp[last[c[i]]]) % mod
    last[c[i]] = i

print dp[-1]