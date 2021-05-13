import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, x, y = map(int, readline().split())
    mat = []

    for _ in range(n):
        a, b, c = map(int, readline().split())
        mat.append((a, b, c))

    dp = [[[INF] * 401 for _ in range(401)] for __ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        a, b, c = mat[i - 1]
        for j in range(401):
            for k in range(401):
                dp[i][j][k] = dp[i - 1][j][k]
                if j - a >= 0 and k - b >= 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - a][k - b] + c)

    ans = INF
    for i, j in zip(range(x, 401, x), range(y, 401, y)):
        ans = min(ans, dp[n][i][j])

    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
