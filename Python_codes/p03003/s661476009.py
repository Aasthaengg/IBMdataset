# https://hiramekun.hatenablog.com/entry/2019/06/18/184256

def main():
    MOD = 10 ** 9 + 7

    N, M = map(int, input().split())
    *s, = map(int, input().split())
    *t, = map(int, input().split())

    dp = [[0] * (M + 1) for _ in range(N + 1)]  # (i,j)で丁度終わる文字列数
    dp[0][0] = 0
    dp[0][1] = 0
    dp[1][0] = 0

    acc = [[0] * (M + 1) for _ in range(N + 1)]
    acc[0][0] = 0
    acc[0][1] = 0
    acc[1][0] = 0

    for i, si in enumerate(s, 1):
        for j, ti in enumerate(t, 1):
            if si == ti:
                dp[i][j] = acc[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            acc[i][j] = (acc[i - 1][j] + acc[i][j - 1] + dp[i][j] - acc[i - 1][j - 1]) % MOD

    ans = acc[N][M] + 1  # ("","")のケース

    print(ans)


if __name__ == '__main__':
    main()
