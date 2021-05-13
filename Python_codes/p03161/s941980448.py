INF = 10**9


def solve():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    # 初期化
    dp = [INF] * N

    # 初期条件
    dp[0] = 0

    # DPループ
    for i in range(1, N):
        for j in range(min(i, K)):
            dp[i] = min(dp[i], dp[i - j - 1] + abs(h[i] - h[i - j - 1]))

    print(dp[-1])


if __name__ == "__main__":
    solve()