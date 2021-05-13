def main():
    """
    1 <= i < j < k <= |T|
    Ti = A
    Tj = B
    Tk = C
    """
    S = input()
    ans2 = dp_simple(S)
    print(ans2)


def dp_simple(S):
    n = len(S)
    MOD = 10 ** 9 + 7
    dp = [[0] * (3+1) for _ in range(n+1)]
    # 組合せ列挙なので掛け算としての単位元
    dp[0][0] = 1

    for i in range(n):
        # i文字目まで
        for j in range(3+1):
            # 0-3文字揃ってる
            m = 1
            if S[i] == "?":
                # 置換できるので3パターン
                m = 3
            dp[i+1][j] += dp[i][j] * m
            dp[i+1][j] %= MOD

            # 3文字揃ってないとき, 対応する文字になるか？
            if j < 3 and (S[i] == "?" or S[i] == "ABC"[j]):
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD

    ans = dp[n][3]
    return ans


if __name__ == '__main__':
    main()
