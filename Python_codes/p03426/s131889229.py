H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
X = [list(map(int, input().split())) for _ in range(Q)]

ctr = {}
for i in range(H):
    for j in range(W):
        ctr[A[i][j]] = (i, j)

memo = [0] * (H * W + 1)
for n in range(D + 1, H * W + 1):
    i, j = ctr[n - D]
    x, y = ctr[n]
    memo[n] = abs(x - i) + abs(y - j) + memo[n - D]

for l, r in X:
    print(memo[r] - memo[l])
