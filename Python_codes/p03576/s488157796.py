def main():
    N, K = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    X, Y = [], []
    for x, y in XY:
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    Xm = {x: i for i, x in enumerate(X)}
    Ym = {y: i for i, y in enumerate(Y)}
    Xr = {i: x for i, x in enumerate(X)}
    Yr = {i: y for i, y in enumerate(Y)}
    cXY = [(Xm[x], Ym[y]) for x, y in XY]
    m = 10 ** 40
    for l in range(N):
        for r in range(l + 1, N):
            for b in range(N):
                for t in range(b + 1, N):
                    k = 0
                    for x, y in cXY:
                        if l <= x <= r and b <= y <= t:
                            k += 1
                    if k >= K:
                        m = min(m, (Xr[r] - Xr[l]) * (Yr[t] - Yr[b]))
    return m
print(main())
