H, W = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]
ans = []
for h in range(H-1):
    for w in range(W):
        if G[h][w] % 2:
            ans.append([h+1, w+1, h+2, w+1])
            G[h][w] -= 1
            G[h+1][w] += 1
for w in range(W-1):
    if G[H-1][w] % 2:
        ans.append([H, w+1, H, w+2])
        G[H-1][w] -= 1
        G[H-1][w+1] += 1
print(len(ans))
for row in ans:
    print(*row)
