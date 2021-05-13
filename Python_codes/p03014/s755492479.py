import sys
input=sys.stdin.readline
H, W = [int(x) for x in input().split()]
board = []
for _ in range(H):
    board.append(input())

L = [[0]*W for _ in range(H)]
R = [[0]*W for _ in range(H)]
U = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if board[i][j] == '.':
            if j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i][j - 1] + 1

for i in range(H):
    for j in reversed(range(W)):
        if board[i][j] == '.':
            if j == W - 1:
                R[i][j] = 1
            else:
                R[i][j] = R[i][j + 1] + 1

for j in range(W):
    for i in range(H):
        if board[i][j] == '.':
            if i == 0:
                U[i][j] = 1
            else:
                U[i][j] = U[i - 1][j] + 1

for j in range(W):
    for i in reversed(range(H)):
        if board[i][j] == '.':
            if i == H - 1:
                D[i][j] = 1
            else:
                D[i][j] = D[i + 1][j] + 1

ans = 0
for i in range(H):
    for j in range(W):
        cand = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
        ans = max(ans, cand)
        
print(ans)