H, W, K = map(int, input().split())
C = [0] * H
for h in range(H):
    C[h] = input()

ans = 0
for tate in range(2 ** H):
    for yoko in range(2 ** W):
        tate_ = tate
        T = []
        for _ in range(H):
            T.append(tate_ % 2 == 0)
            tate_ //= 2
        Y = []
        yoko_ = yoko
        for _ in range(W):
            Y.append(yoko_ % 2 == 0)
            yoko_ //= 2
#         print(tate, T, yoko, Y)
        count = 0
        for h in range(H):
            if T[h]: continue
            for w in range(W):
                if Y[w]: continue
                if C[h][w] == '#':
                    count += 1
        if count == K:
            ans += 1
print(ans)