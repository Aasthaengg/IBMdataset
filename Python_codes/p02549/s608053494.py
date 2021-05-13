n, k = map(int, input().split())
lr = []
for _ in range(k):
    l, r = map(int, input().split())
    lr.append((l, r))
mod = 998244353
dp = [0]*(2*n+1)
dp[0] = 1
dp[1] = -1
now = 1
for i in range(n-1):
    for l, r in lr:
        dp[i+l] += now
        dp[i+r+1] -= now
    now += dp[i+1]
    now %= mod
print(now)