
import sys
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
ans = []

for i in range(H):
    if i % 2 == 0:
        for j in range(W - 1):
            if X[i][j] % 2 == 1:
                X[i][j] -= 1
                X[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))

        if X[i][-1] % 2 == 1 and i < H - 1:
            X[i][-1] -= 1
            X[i + 1][-1] += 1
            ans.append((i + 1, W, i + 2, W))
    else:
        for j in reversed(range(1, W)):
            if X[i][j] % 2 == 1:
                X[i][j] -= 1
                X[i][j - 1] += 1
                ans.append((i + 1, j + 1, i + 1, j))

        if X[i][0] % 2 == 1 and i < H - 1:
            X[i][0] -= 1
            X[i + 1][0] += 1
            ans.append((i + 1, 1, i + 2, 1))

print(len(ans))
for t in ans:
    print(*t)
