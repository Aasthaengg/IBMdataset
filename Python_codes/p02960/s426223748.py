import sys

input = sys.stdin.readline

P = 10 ** 9 + 7
Q = 13


def main():
    S = input().rstrip()

    N = len(S)
    dp = [[0] * Q for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        D = S[i]
        if D == "?":
            for d in range(10):
                for j in range(Q):
                    dp[i + 1][(10 * j + d) % Q] += dp[i][j]
        else:
            d = int(D)
            for j in range(Q):
                dp[i + 1][(10 * j + d) % Q] += dp[i][j]

        for j in range(Q):
            dp[i + 1][j] %= P

    ans = dp[N][5]
    print(ans)


if __name__ == "__main__":
    main()
