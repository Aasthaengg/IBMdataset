H, W, A, B = map(int, input().split())

Ans = [['0'] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i < B and j < A:
            Ans[i][j] = 1
        if i >= B and j >= A:
            Ans[i][j] = 1
        print(Ans[i][j], end='')
    print()