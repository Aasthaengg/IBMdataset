def e_common_subsequence(N, M, S, T, MOD=10**9 + 7):
    # dp[i][j]: S[i], T[j] まで考慮したとき、この2つをペアにしたときの場合の数
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    total = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        total[i][0] = 1
    for j in range(M + 1):
        total[0][j] = 1

    ans = 1  # 空の列は常に等しい列である
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i + 1][j + 1] = (total[i][j] % MOD)
                ans += dp[i + 1][j + 1]
            total[i + 1][j + 1] = (total[i][j + 1] + total[i + 1][j]
                                   - total[i][j] + dp[i + 1][j + 1] + MOD) % MOD
    return ans % MOD

N, M = [int(i) for i in input().split()]
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]
print(e_common_subsequence(N, M, S, T))