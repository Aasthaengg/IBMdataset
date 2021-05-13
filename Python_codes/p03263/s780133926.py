import sys

H, W = map(int, input().split())
A = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(H)]

res = []
for i in range(H):
    for j in range(W):
        if A[i][j] % 2 != 0 and j < W - 1:
            A[i][j] -= 1
            A[i][j + 1] += 1
            res.append([i + 1, j + 1, i + 1, j + 2])
        elif A[i][j] % 2 != 0 and i != H - 1 and j == W - 1:
            A[i][j] -= 1
            A[i + 1][j] += 1
            res.append([i + 1, j + 1, i + 2, j + 1])
print(len(res))
for i in range(len(res)):
    print(*res[i])
