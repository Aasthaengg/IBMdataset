def main():
    MOD = 10 ** 9 + 7

    EQ = 0  # 等しくなり得る
    SMALL = 1  # 未満確定

    S = map(int, input())
    dp = [1, 0]
    for x in S:
        ndp = [0] * 2

        if x == 0:
            ndp[EQ] = dp[EQ]  # (0,0)
            ndp[SMALL] = dp[SMALL] * 3  # (0,0),(0,1),(1,0)
        elif x == 1:
            ndp[EQ] = dp[EQ] * 2  # (0,1),(1,0)
            ndp[SMALL] = dp[EQ] + dp[SMALL] * 3  # EQ->(0,0), SMALL->(0,0),(0,1),(1,0)

        *dp, = map(lambda x: x % MOD, ndp)

    ans = sum(dp) % MOD  # 取り忘れ

    print(ans)


if __name__ == '__main__':
    main()
