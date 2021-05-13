import sys


sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()
    N = len(S)
    dp = [[0] * 13 for _ in range(N)]

    if S[-1] == "?":
        for i in range(10):
            dp[0][i] = 1
    else:
        dp[0][int(S[-1])] = 1

    tenfactor = 1
    for i in range(1, N):
        tenfactor *= 10
        tenfactor %= 13

        if S[N - i - 1] != "?":
            for k in range(13):
                j = int(S[N - i - 1])
                idx = (k + j * tenfactor) % 13
                dp[i][idx] += dp[i - 1][k]
                dp[i][idx] %= MOD
        else:
            for j in range(10):
                for k in range(13):
                    idx = (k + j * tenfactor) % 13
                    dp[i][idx] += dp[i - 1][k]
                    dp[i][idx] %= MOD

    print(dp[-1][5])


if __name__ == "__main__":
    main()
