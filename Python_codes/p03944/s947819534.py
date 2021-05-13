W, H, N = map(int, input().split())

board = [[1]*W for _ in range(H)]

for _ in range(N):
    x, y, a = map(int, input().split())
    t = 0
    b = H
    l = 0
    r = W
    if a == 1:
        r = x
    if a == 2:
        l = x
    if a == 3:
        b = y
    if a == 4:
        t = y
    
    for h in range(t, b):
        for w in range(l, r):
            board[h][w] = 0
    
print(sum([sum(r) for r in board]))