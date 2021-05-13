R, C, K = map(int, input().split())

V = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    V[r][c] = v

dp0 = [[0]*(C+1) for _ in range(R+1)]
dp1 = [[0]*(C+1) for _ in range(R+1)]
dp2 = [[0]*(C+1) for _ in range(R+1)]
dp3 = [[0]*(C+1) for _ in range(R+1)]
for i in range(R+1):
    for j in range(C+1):
        v = V[i][j]

        a = dp0[i][j]
        b = dp0[i][j]
        c = dp0[i][j]
        d = dp0[i][j]

        pa = pb = pc = pd = 0
        if i > 0:
            pa = dp0[i-1][j]
            pb = dp1[i-1][j]
            pc = dp2[i-1][j]
            pd = dp3[i-1][j]

        la = lb = lc = ld = 0
        if j > 0:
            la = dp0[i][j-1]
            lb = dp1[i][j-1]
            lc = dp2[i][j-1]
            ld = dp3[i][j-1]

        a = max(a, pa)
        b = max(b, pa+v)
        a = max(a, la)

        a = max(a, pb)
        b = max(b, pb+v)
        b = max(b, lb, la+v)

        a = max(a, pc)
        b = max(b, pc+v)
        c = max(c, lc, lb+v)

        a = max(a, pd)
        b = max(b, pd+v)
        d = max(d, ld, lc+v)

        dp0[i][j] = a
        dp1[i][j] = b
        dp2[i][j] = c
        dp3[i][j] = d

print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))
