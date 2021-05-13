H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
ans = 0
for case in range(2**(H+W)):
    black = 0
    for i in range(H):
        for j in range(W):
            if (case >> i) & 1 and (case >> j + H) & 1 and c[i][j] == "#":
                black += 1
    if black == K:
        ans += 1
print(ans)