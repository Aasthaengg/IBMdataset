
def resolve():
    INF = 10 ** 18
    N, M = map(int, input().split())

    Box_key = []
    for i in range(M):
        a, b = map(int, input().split())
        C = list(map(int, input().split()))
        s = sum(1 << (c - 1) for c in C)
        Box_key.append((s, a))

    # dp[i]: 集合iの宝箱を開ける最小コスト
    dp = [INF] * (1 << N)
    dp[0] = 0

    for s in range(1 << N):
        for i in range(M):
            ns = s | Box_key[i][0]
            cost = dp[s] + Box_key[i][1]
            dp[ns] = min(dp[ns], cost)

    if dp[(1 << N) - 1] == INF:
        print(-1)
    else:
        print(dp[(1 << N) - 1])


if __name__ == "__main__":
    resolve()