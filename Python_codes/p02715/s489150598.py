N, K = map(int, input().split())
MOD = 10 ** 9 + 7

# dp[i] := gcdがiになるようなものの通り数
dp = [0] * (K + 1)
for k in reversed(range(1, K + 1)):
    cnt = pow(K // k, N, MOD)
    for i in range(2, K + 1):
        if i * k > K:
            break
        cnt -= dp[i * k]
    dp[k] = cnt

ans = 0
for k, cnt in enumerate(dp):
    ans += k * cnt
    ans %= MOD
print(ans % MOD)
