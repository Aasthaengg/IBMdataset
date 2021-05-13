def resolve():
    Nyens, Mtypes = map(int, input().split())  # N円をM種類のコインで最小枚数で払うという問題
    types = list(map(int, input().split()))  # 何円玉があるかのリスト

    def knapsack(Nyens, Mtypes, types):
        # dp[i][j]:i種類目までのコイン限定でj円払うのに必要な最小枚数
        # 最小で無限枚必要として初期化
        dp = [[float('inf')] * (Nyens + 1) for _ in range(Mtypes + 1)]

        # 0円は0枚で払える
        for ii in range(Mtypes):
            dp[ii][0] = 0

        for i in range(Mtypes):
            for j in range(Nyens + 1):
                if j >= types[i]:  # 最小枚数更新の可能性
                    dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - types[i]] + 1)
                else:  # 可能性なし
                    dp[i + 1][j] = dp[i][j]

        return dp[Mtypes][Nyens]

    print(knapsack(Nyens, Mtypes, types))

resolve()
