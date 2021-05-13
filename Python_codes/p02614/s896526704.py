H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

ans = 0
for hselection in range(1 << H):
    for wselection in range(1 << W):
        count = 0
        for h in range(H):
            for w in range(W):
                if hselection & (1 << h) or wselection & (1 << w):
                    continue
                if C[h][w] == "#":
                    count += 1
        if count == K:
            ans += 1
print(ans)