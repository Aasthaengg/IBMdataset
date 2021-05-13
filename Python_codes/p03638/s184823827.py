H, W = map(int, input().split())
N = int(input())
A = tuple(map(int, input().split()))

Table = [[None] * W for _ in range(H)]
h, w = 0, 0
for i, a in enumerate(A):
    for x in range(a):
        Table[h][w] = i + 1
        if h % 2:
            if w == 0:
                h += 1
            else:
                w -= 1
        else:
            if w == W - 1:
                h += 1
            else:
                w += 1
for t in Table:
    print(*t)
