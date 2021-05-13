def abc119_d():
    import sys
    read = sys.stdin.buffer.read
    inp = iter(map(int, read().split()))

    a = next(inp)
    b = next(inp)
    q = next(inp)
    S = [next(inp) for _ in range(a)]
    T = [next(inp) for _ in range(b)]

    from bisect import bisect_left
    inf = 10**12

    for _ in range(q):
        x = next(inp)
        si = bisect_left(S, x)
        ti = bisect_left(T, x)

        sl, sr = inf, inf
        tl, tr = inf, inf
        if 0 < si: sl = x - S[si-1]
        if si < a: sr = S[si] - x
        if 0 < ti: tl = x - T[ti-1]
        if ti < b: tr = T[ti] - x

        ans = inf
        ans = min(ans, max(sl, tl))
        ans = min(ans, max(sr, tr))
        ans = min(ans, 2 * min(sl, tr) + max(sl, tr))
        ans = min(ans, 2 * min(sr, tl) + max(sr, tl))
        print(ans)

if __name__ == '__main__':
    abc119_d()