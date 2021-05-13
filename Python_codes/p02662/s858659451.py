n, s = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353

dp = [0 for _ in range(s+1)]
dp[0] = 1

for i in range(n):
    plus = [dp[j-a[i]]  if j-a[i] >=0 else 0 for j in range(s+1)]
    for j in range(s+1):
        dp[j] = (dp[j]*2 +plus[j])%mod

print(dp[s])