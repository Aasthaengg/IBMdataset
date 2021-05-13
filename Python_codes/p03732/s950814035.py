import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def solve1(N, W, weight, value):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - weight[i] >= 0:
                dp[i + 1][w] = dp[i][w - weight[i]] + value[i]
            if dp[i + 1][w] < dp[i][w]:
                dp[i + 1][w] = dp[i][w]

    return dp[N][W]


def solve2(N, W, weight, value):
    w0 = weight[0]
    M = W // w0
    if M == 0:
        return 0

    weight_adj = [w - w0 for w in weight]
    w_total = sum(weight_adj)

    dp = [[[0] * (w_total + 1) for j in range(N + 1)] for i in range(M + 1)]
    for i in range(M):
        for j in range(N):
            for w in range(w_total + 1):
                if w - weight_adj[j] >= 0:
                    dp[i + 1][j + 1][w] = dp[i][j][w - weight_adj[j]] + value[j]
                if dp[i + 1][j + 1][w] < dp[i + 1][j][w]:
                    dp[i + 1][j + 1][w] = dp[i + 1][j][w]
                if dp[i + 1][j + 1][w] < dp[i][j + 1][w]:
                    dp[i + 1][j + 1][w] = dp[i][j + 1][w]

    return max(dp[M][N][min(W - w0 * M, w_total)], dp[M - 1][N][min(W - w0 * (M - 1), w_total)])


def main():
    N, W, *wv = map(int, read().split())
    weight = wv[::2]
    value = wv[1::2]

    if weight[0] < 500:
        ans = solve1(N, W, weight, value)
    else:
        ans = solve2(N, W, weight, value)

    print(ans)
    return


if __name__ == '__main__':
    main()
