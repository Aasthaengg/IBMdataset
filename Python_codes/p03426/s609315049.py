H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

d = {}
for y in range(H):
    Ay = A[y]
    for x in range(W):
        d[Ay[x]] = (y, x)

t = [[0] * (H * W // D + 1) for _ in range(D)]
for i in range(D):
    ti = t[i]
    j = 0
    if i == 0:
        j = 1
    while i + (j + 1) * D <= H * W:
        y1, x1 = d[i + j * D]
        y2, x2 = d[i + (j + 1) * D]
        ti[j + 1] = abs(y1 - y2) + abs(x1 - x2)
        j += 1
    for j in range(len(ti) - 1):
        ti[j + 1] += ti[j]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    i = L % D
    print(t[i][(R - i) // D] - t[i][(L - i) // D])
