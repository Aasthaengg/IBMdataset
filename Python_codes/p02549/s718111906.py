def resolve():
    MOD = 998244353
    N, K = map(int, input().split())
    S = [tuple(map(int, input().split())) for _ in range(K)]
    L = [0] * K
    R = [0] * K
    L, R = zip(*S)

    dp = [0] * (N + 1)
    dp[1] = 1

    dp_acum = [0] * (N + 1)
    dp_acum[1] = 1

    for i in range(2, N + 1):
        for j in range(K):
            li = i - R[j]
            ri = i - L[j]
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dp_acum[ri] - dp_acum[li - 1]
            dp[i] %= MOD

        dp_acum[i] = dp_acum[i - 1] + dp[i]
        dp_acum[i] %= MOD

    print(dp[N])


if __name__ == "__main__":
    resolve()
