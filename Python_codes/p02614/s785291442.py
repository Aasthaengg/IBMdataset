H, W, K = map(int, input().split())
c = []
for i in range(H):
    c.append(list(input()))

ans = 0

for mass_H in range(1 << H):
    for mass_W in range(1 << W):
        black = 0
        for i in range(H):
            for j in range(W):
                if ((mass_H >> i) & 1) == 0 and ((mass_W >> j ) & 1) == 0 and c[i][j] == '#':
                    black += 1
        if black == K:
            ans += 1

print(ans)
