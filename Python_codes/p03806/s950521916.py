INF = 10**18

def solve(N, Ma, Mb, sol):
    if N % 2 == 1:
        sol.append((0, 0, 0))
        N += 1

    M = N // 2

    sol1 = sol[:M]
    sol2 = sol[M:]

    S1 = []
    D = dict()
    res = INF

    for i in range(2**M):
        A1, B1, C1 = 0, 0, 0
        A2, B2, C2 = 0, 0, 0
        for j in range(M):
            if (i >> j) & 1:
                a1, b1, c1 = sol1[j]
                a2, b2, c2 = sol2[j]
                A1 += a1
                B1 += b1
                C1 += c1
                A2 += a2
                B2 += b2
                C2 += c2
        S1.append((A1, B1, C1))
        x = Mb * A2 - Ma * B2
        if x == 0 and C2 > 0:
            res = min(res, C2)
        if not x in D or 0 < C2 < D[x]:
            D[x] = C2

    for i in range(2**M):
        a, b, c = S1[i]
        x = Ma * b - Mb * a
        if x == 0 and c > 0:
            res = min(res, c)
        if x in D and D[x] + c > 0:
            res = min(res, D[x] + c)

    return res

N, Ma, Mb = map(int, input().split())
sol = [tuple(map(int, input().split())) for _ in range(N)]

res = solve(N, Ma, Mb, sol)

print(res if res != INF else -1)