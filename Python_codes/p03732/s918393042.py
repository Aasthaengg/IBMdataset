

def submit():
    n, w = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    
    if items[0][0] > w:
        print(0) # 1個も選べない
        return

    if sum([e[0] for e in items]) <=  w:
        print(sum([e[1] for e in items])) # 全部選べる
        return

    # 以降、必ず1個は選ぶ
    # かつbase_weight <= W < all_weight
    base_weight = items[0][0]
    
    # dp[i][j][k] : i番目までのアイテムのうち、j個を選んだ時、weight kで最大価値
    # weightはbase_weightからの差分をカウントする
    # dp[i + 1][j][k] = 
    #   dp[i][j][k], dp[i][j - 1][k - (w - base_weight)]
    # j * base_weight + k <= wの範囲で計算する
    
    dp = [[[0 for _ in range(3 * n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        rw = items[i - 1][0] - base_weight
        v = items[i - 1][1]
        for j in range(i + 1):
            for k in range(3 * n + 1):
                if j * base_weight + k <= w:
                    if j - 1 >= 0 and k - rw >= 0:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - 1][k - rw] + v)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                else:
                    break

    ans = 0
    for j in range(n + 1):
        for k in range(3 * n + 1):
            ans = max(ans, dp[n][j][k])
    print(ans)

submit()