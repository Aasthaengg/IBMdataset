def f_knapsack_for_all_subsets(MOD=998244353):
    N, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    # dp[i][j]: i 番目の要素を見たとき、和が j であるような場合の数
    dp = [[0 for j in range(S + 1)] for i in range(N + 1)]
    dp[0][0] = 1  # インデックスの集合が空のとき、和は 0 の 1 通り
    for i, a in enumerate(A):
        for j in range(S + 1):
            # editorial でいうところの選択肢 2, 3 に相当するので、2 倍
            dp[i + 1][j] += 2 * dp[i][j]
            dp[i + 1][j] %= MOD
            if j + a <= S:  # 選択肢 1
                dp[i + 1][j + a] += dp[i][j]
                dp[i + 1][j + a] %= MOD
    return dp[N][S]

print(f_knapsack_for_all_subsets())