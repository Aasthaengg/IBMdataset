H, W, A, B = map(int, input().split())
board1 = [[0] * A + [1] * (W - A) for _ in range(B)]
for l in board1:
    print(*l, sep='')
board2 = [[1] * A + [0] * (W - A) for _ in range(H - B)]
for l in board2:
    print(*l, sep='')
