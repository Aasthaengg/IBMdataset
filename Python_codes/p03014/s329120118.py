def m():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    Gx = [[-1 for _ in range(W)] for _ in range(H)]
    Gy = [[-1 for _ in range(W)] for _ in range(H)]

    for a in range(H):
        left = 0
        for b in range(W):
            if S[a][b] == '#':
                left = 0
            else:
                Gx[a][b] = left + 1
                left = Gx[a][b]
    for b in range(W):
        top = 0
        for a in range(H):
            if S[a][b] == '#':
                top = 0
            else:
                Gy[a][b] = top + 1
                top = Gy[a][b]

    for i in reversed(range(H)):
        right = 0
        for j in reversed(range(W)):
            if Gx[i][j] == -1:
                right = 0
            else:
                Gx[i][j] = max(Gx[i][j], right)
                right = Gx[i][j]

    for j in reversed(range(W)):
        bot = 0
        for i in reversed(range(H)):
            if Gy[i][j] == -1:
                bot = 0
            else:
                Gy[i][j] = max(Gy[i][j], bot)
                bot = Gy[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(Gx[i][j] + Gy[i][j], ans)
    return ans - 1


print(m())
