mod = 998244353
N, K = map(int, input().split())

S = []
for i in range(K):
    L, R = map(int, input().split())
    S.append((L, R))

dp = [0] * (N+1)
dpsum = [0] * (N+1)
dp[1] = 1
dpsum[1] = 1

for i in range(2, N+1):
    for s in S:
        l = i - s[1]
        r = i - s[0]
        if r < 1:continue
        l = max(1, l)

        dp[i] += dpsum[r] - dpsum[l-1]
        dp[i] %= mod

    dpsum[i] = (dpsum[i-1] + dp[i]) % mod

print(dp[-1])
