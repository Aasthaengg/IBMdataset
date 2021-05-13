n, k = map(int, input().split())
L, R = [], []
MOD = 998244353
for _ in range(k):
    t1, t2 = map(int, input().split())
    L.append(t1)
    R.append(t2)

dp = [0] * (n+1)
dp[1] = 1
acc = [0] * (n+1)
acc[1] = 1

for idx1 in range(2, n+1):
    for idx2 in range(k):
        if idx1 - L[idx2] < 0:
            continue
        dp[idx1] += (acc[idx1-L[idx2]] - acc[max(0, idx1-R[idx2]-1)]) % MOD
        dp[idx1] %= MOD
    acc[idx1] = (acc[idx1-1] + dp[idx1]) % MOD

print(dp[-1])