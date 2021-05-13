def abc061_d():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    inf = float("inf")
    result = [inf] * n
    result[0] = 0

    for i in range(n - 1):
        for f, t, c in edges:
            result[t - 1] = min(result[t - 1], result[f - 1] - c)
    ans = result[n - 1]
    for f, t, c in edges:
        result[t - 1] = min(result[t - 1], result[f - 1] - c)
    print(-ans if ans == result[n - 1] else "inf")


if __name__ == '__main__':
    abc061_d()
