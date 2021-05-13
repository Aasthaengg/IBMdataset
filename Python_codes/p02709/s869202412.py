def e_active_infants():
    # 参考: https://kmjp.hatenablog.jp/entry/2020/04/20/0900
    N = int(input())
    A = [int(i) for i in input().split()]
    # どこから移動するかの情報が必要なので、付与する
    p = sorted([(a, k) for k, a in enumerate(A)], reverse=True)

    # dp[x][y]: 元の場所から (元の場所を含んで) 左に動いた人数が x 人、
    # 右に動いた人数が y 人のときのうれしさの最大値
    dp = [[-float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0  # 誰も動いていなければうれしさは 0
    for i in range(N):
        a, r = p[i]
        for x in range(i + 1):
            y = i - x
            # 左右の埋まっていない端に動かしたときの場合の遷移
            dp[x + 1][y] = max(dp[x + 1][y], dp[x][y] + abs(r - x) * a)
            dp[x][y + 1] = max(dp[x][y + 1], dp[x][y] + abs(r - (N - 1 - y)) * a)
    return max(dp[i][N - i] for i in range(N + 1))

print(e_active_infants())