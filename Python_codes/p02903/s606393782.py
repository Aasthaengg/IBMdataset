H, W, A, B = map(int, input().split())
ret = [[0] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if w < A and h < B:
            ret[h][w] = 1
        elif w >= A and h >= B:
            ret[h][w] = 1

for row in ret:
    print(''.join([str(i) for i in row]))
