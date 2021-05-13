# 解説AC
MOD = 10**9 + 7


def main():
    S = [s for s in input()[::-1]]
    N = len(S)
    dp = [[0]*13 for i in range(N+1)]
    dp[0][0] = 1
    d = 1
    for i in range(N):
        for j in range(13):
            if S[i] != "?":
                a = int(S[i])
                ne = ((a*d)+j) % 13
                dp[i+1][ne] += dp[i][j]
                dp[i+1][ne] %= MOD
            else:
                for k in range(10):
                    ne = ((k*d)+j) % 13
                    dp[i+1][ne] += dp[i][j]
                    dp[i+1][ne] %= MOD
        d *= 10
        d %= 13
    print(dp[N][5] % MOD)


if __name__ == '__main__':
    main()
