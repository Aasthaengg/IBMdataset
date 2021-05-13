import numpy as np

W, H, N = map(int, input().split())
F = np.ones((H, W), dtype = int)

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(H):
            for j in range(x):
                if F[i][j] == 1:
                    F[i][j] = 0
    if a == 2:
        for i in range(H):
            for j in range(x, W):
                if F[i][j] == 1:
                    F[i][j] = 0
    if a == 3:
        for i in range(y):
            for j in range(W):
                if F[i][j] == 1:
                    F[i][j] = 0
    if a == 4:
        for i in range(y, H):
            for j in range(W):
                if F[i][j] == 1:
                    F[i][j] = 0

print(sum(sum(F)))
