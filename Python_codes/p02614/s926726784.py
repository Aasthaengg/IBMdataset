H, W, K = map(int, input().split())

field = [input() for _ in range(H)]

ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        tmp = 0
        for i2 in range(H):
            for j2 in range(W):
                if (i >> i2) & 1: continue
                if (j >> j2) & 1: continue
                if field[i2][j2] != '#': continue
                tmp += 1
        if tmp == K: ans += 1

print(ans)                 
