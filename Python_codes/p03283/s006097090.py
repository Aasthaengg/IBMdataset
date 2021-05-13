# 79
# ABC106 D


def solve():
    N, M, Q = map(int, input().split())
    LR_L = tuple([int(x) for x in input().split()] for y in range(M))
    Q_L = tuple([int(x) for x in input().split()] for y in range(Q))

    imos_l = [[0] * (N+2) for _ in range(N+1)]

    for l, r in LR_L:
        imos_l[l][l] += 1
        imos_l[l][r+1] -= 1
    for i in range(1, N+1):
        for j in range(1, N+2):
            imos_l[i][j] += imos_l[i][j-1]

    for p, q in Q_L:
        ans = 0
        for i in range(p, q+1):
            ans += imos_l[i][i] - imos_l[i][q+1]
        print(ans)


solve()
