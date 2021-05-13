def main():
    from itertools import permutations, tee

    INF = 1 << 30

    N, M, R = map(int, input().split())
    *r, = (int(x) - 1 for x in input().split())

    d = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        d[a][b] = d[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(
                    d[i][j],
                    d[i][k] + d[k][j]
                )

    ans = INF
    for perm in permutations(r):
        perm_iter = iter(perm)
        frm_iter, to_iter = tee(perm_iter, 2)
        next(to_iter)
        t = 0
        for frm, to in zip(frm_iter, to_iter):
            t += d[frm][to]
        ans = min(ans, t)
    print(ans)


if __name__ == '__main__':
    main()
