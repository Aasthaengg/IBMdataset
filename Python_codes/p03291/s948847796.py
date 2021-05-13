def main():
    """
    1 <= i < j < k <= |T|
    Ti = A
    Tj = B
    Tk = C
    """
    S = input()
    ans = editorial(S)

    print(ans)


def editorial(S):
    MOD = 10 ** 9 + 7
    n = len(S)
    dp = [[0] * (3+1) for _ in range(n+1)]

    for i in range(n, -1, -1):
        for j in range(3, -1, -1):
            if i == n:
                x = int(j == 3)
                # ≠3: 丸を3個つける前に最後の文字まで見終わってしまい、手遅れ
                # =3: 処理が正常終了
                dp[i][j] = x
            else:
                m1 = 1
                if S[i] == "?":
                    m1 = 3

                if j == 3:
                    # 丸は3個つけ終わったので、あとは?を置換するのみ
                    dp[i][j] = m1 * dp[i+1][j]
                else:
                    m2 = int(S[i] == "?" or S[i] == "ABC"[j])
                    # 前半:i文字目に丸をつけない場合, 後半:丸をつける場合に対応
                    dp[i][j] = m1 * dp[i+1][j] + m2 * dp[i+1][j+1]

                dp[i][j] %= MOD

    ans = dp[0][0]
    return ans


if __name__ == '__main__':
    main()
