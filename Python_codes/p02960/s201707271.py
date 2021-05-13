import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    S = input()
    MOD = 10 ** 9 + 7
    dp = [[0] * 13 for _ in range(len(S) + 1)]
    dp[0][0] = 1
    mul = 1
    for i in range(len(S)):
        x = S[-(i + 1)]
        if x == "?":
            for k in range(10):
                for j in range(13):
                    dp[i + 1][(mul * k + j) % 13] += dp[i][j]
                    dp[i + 1][(mul * k + j) % 13] %= MOD
        else:
            k = int(x)
            for j in range(13):
                dp[i + 1][(mul * k + j) % 13] += dp[i][j]
                dp[i + 1][(mul * k + j) % 13] %= MOD
        mul = mul * 10 % 13
    print(dp[len(S)][5])


if __name__ == "__main__":
    main()
