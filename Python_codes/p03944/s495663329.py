W, H, N = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(N)]

S = [[1] * W for _ in range(H)]
for x, y, a in xya:
    if a == 1:
        for i in range(H):
            for j in range(x):
                S[i][j] = 0
    elif a == 2:
        for i in range(H):
            for j in range(x, W):
                S[i][j] = 0
    elif a == 3:
        for i in range(y):
            for j in range(W):
                S[i][j] = 0
    else:
        for i in range(y, H):
            for j in range(W):
                S[i][j] = 0
A = 0
for i in range(H):
    A += sum(S[i])
print(A)