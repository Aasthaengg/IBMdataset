def e_payment():
    N = input()

    dp = (0, 1)  # 「最下位桁の 1 つ下の桁」を仮想した場合分けを省くための初期化
    for k, ch in enumerate(N[::-1]):  # 最下位の桁から見る
        n = int(ch)
        t1, t2 = dp
        a = min(t1 + n, t2 + n + 1)
        b = min(t1 + (10 - n), t2 + (10 - (n + 1)))
        dp = (a, b)
    return min(dp[0], dp[1] + 1)

print(e_payment())