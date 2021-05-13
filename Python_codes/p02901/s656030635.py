
def resolve():
    INF = 10 ** 18
    N, M = map(int, input().split())

    Cost = [0] * M
    Box_key = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        Cost[i] = a
        C = list(map(int, input().split()))
        Box_key[i] = sum(1 << (c - 1) for c in C)

    # dp[ i ][ S ] := 最初の i 個の鍵からいくつか選んで、
    # 開いた宝箱の集合が S で表されるような場合についての、最小コスト
    dp = [[INF] * (1 << N) for _ in range(M + 1)]
    dp[0][0] = 0

    for i in range(M):
        for j in range(1 << N):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            dp[i + 1][j | Box_key[i]] = min(dp[i + 1][j | Box_key[i]], dp[i][j] + Cost[i])

    if dp[M][(1 << N) - 1] == INF:
        print(-1)
    else:
        print(dp[M][(1 << N) - 1])


if __name__ == "__main__":
    resolve()