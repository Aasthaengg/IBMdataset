MOD = 10**9 + 7


def main():
    S = input()
    N = len(S)
    dp = [[0]*13 for _ in range(N+1)]
    dp[0][0] = 1
    from itertools import product
    for i, mod13 in product(range(N), range(13)):
        if S[i] == "?":
            lim = 9
            for d in range(lim+1):
                dp[i+1][(mod13*10 + d) % 13] \
                    += dp[i][mod13]
                dp[i+1][(mod13*10 + d) % 13] \
                    %= MOD
        else:
            d = int(S[i])
            dp[i+1][(mod13*10 + d) % 13] \
                += dp[i][mod13]
            dp[i+1][(mod13*10 + d) % 13] \
                %= MOD
    print(dp[N][5] % MOD)


if __name__ == '__main__':
    main()
