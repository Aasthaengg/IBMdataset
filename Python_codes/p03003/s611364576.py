# coding: utf-8
MOD = int(1e9 + 7)

def f(N, M, s, t):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    cums = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = 0 if s[i-1] != t[j-1] else (cums[i-1][j-1] + 1) % MOD
            cums[i][j] = cums[i-1][j] + cums[i][j-1] - cums[i-1][j-1] + dp[i][j]
    return((cums[N][M] + 1) % MOD)

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
print(f(n, m, s, t))
