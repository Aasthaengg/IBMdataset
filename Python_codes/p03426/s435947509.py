H, W, D = map(int, input().split())
C = [None] * (H * W + 1)
for h in range(H):
    m = map(int, input().split())
    for w, x in enumerate(m):
        C[x] = (h, w)

Acc = [[0] for _ in range(D)]
for i in range(D):
    x = i + 1
    while x + D <= H * W:
        Acc[i].append(Acc[i][-1] + abs(C[x + D][0] - C[x][0]) + abs(C[x + D][1] - C[x][1]))
        x += D

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    tmp = Acc[l % D - 1]
    print(tmp[(r - 1) // D] - tmp[(l - 1) // D])
