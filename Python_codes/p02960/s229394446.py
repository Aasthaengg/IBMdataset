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
        base = pow(10, N - 1 - i, Q)
        D = S[i]
        if D == "?":
            for d in range(10):
                n = d * base
                for j in range(Q):
                    next_j = (j + n) % Q
                    dp[i + 1][next_j] += dp[i][j]
                    dp[i + 1][next_j] %= P
        else:
            n = int(D) * base
            for j in range(Q):
                next_j = (j + n) % Q
                dp[i + 1][(j + n) % Q] += dp[i][j]
                dp[i + 1][(j + n) % Q] %= P

    ans = dp[N][5]
    print(ans)


if __name__ == "__main__":
    main()
