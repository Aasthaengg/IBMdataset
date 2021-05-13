H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = 0
for maskR in range(1 << H):
    for maskC in range(1 << W):
        black = 0
        for i in range(H):
            for j in range(W):
                if ((maskR >> i) & 1) == 0 and ((maskC >> j) & 1) == 0 and C[i][j] == '#':
                    black += 1
        if black == K:
            ans += 1
print(ans)