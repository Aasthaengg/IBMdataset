def main():
    n = int(input())
    p = tuple(map(float, input().split()))
    # pr = [1 - pi for pi in p]
    # DPの二次元配列を行i1＝コインの枚数、列i2＝表がでたコインの枚数、で構築する。
    # DP[][]の初期値は0。ただし0列(表が0枚になる確率)をまず初期化する。
    # DP[i1][i2]の値は、DP[i1-1][i2] * pr + DP[i1-1][i2-1] * p
    # 「表の枚数＞裏の枚数になる確率」は、DPの最下行のX列から右の列の価の合計。
    dp = [[0.0] * (n + 1) for _ in range(n + 1)]
    # ０列目を初期化する。
    dp[0][0] = 1.0 #コイン0枚目で表が０枚の確率＝１
    for i0 in range(1, n + 1):
        dp[i0][0] = dp[i0-1][0] * (1 - p[i0-1])

    for i1 in range(1, n + 1):
        pe = p[i1 - 1]
        pre = 1 - pe
        for i2 in range(1, i1 + 1):
            dp[i1][i2] = dp[i1-1][i2] * pre + dp[i1-1][i2-1] * pe

    r = sum(dp[n][n//2+1:])
    print(r)

if __name__ == '__main__':
    main()