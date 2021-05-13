H, W, A, B = map(int, input().split())

G = [['0'] * W for _ in range(H)]
for h in range(H - B):
    for w in range(W - A):
        G[h][w] = '1'
for h in range(H - B, H):
    for w in range(W - A, W):
        G[h][w] = '1'

for row in G:
    print(''.join(row))

