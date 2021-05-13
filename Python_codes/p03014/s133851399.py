def resolve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    hs = [[0]*w for _ in range(h)]
    ws = [[0]*w for _ in range(h)]

    for i in range(h):
        cums = 0
        for j in range(w):
            if s[i][j] == "#":
                cums = 0
                ws[i][j] = 0
            else:
                cums += 1
                ws[i][j] = cums
        for j in reversed(range(w-1)):
            if ws[i][j+1] != 0 and ws[i][j] != 0:
                ws[i][j] = ws[i][j+1]

    for i in range(w):
        cums = 0
        for j in range(h):
            if s[j][i] == "#":
                cums = 0
                hs[j][i] = 0
            else:
                cums += 1
                hs[j][i] = cums
        for j in reversed(range(h-1)):
            if hs[j+1][i] != 0 and hs[j][i] != 0:
                hs[j][i] = hs[j+1][i]

    ans = 0
    for i in range(h):
        for j in range(w):
            ans = max(ans, ws[i][j] + hs[i][j])
    print(ans-1)
resolve()