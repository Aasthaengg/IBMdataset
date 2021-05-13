H, W, D = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

P = {}

for i in range(H):
    for j in range(W):
        P[A[i][j] - 1] = (i, j)

cum = [0] * (H * W + 1)

for a in range(H * W - D):
    i, j = P[a]
    x, y = P[a + D]
    cum[a + D] = cum[a] + abs(x - i) + abs(y - j)

Q = int(input())
ans = []

for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(cum[r - 1] - cum[l - 1])

print('\n'.join(map(str, ans)))