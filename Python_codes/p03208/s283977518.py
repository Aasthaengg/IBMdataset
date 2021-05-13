def resolve():
    N, K = list(map(int, input().split()))
    h = [int(input()) for _ in range(N)]
    ans = 10 ** 10
    h.sort()

    for i in range(N - K + 1):
        res = h[i+K-1] - h[i]
        ans = min(ans, res)
    print(ans)
    return


resolve()
