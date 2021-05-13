import sys
sys.stdin.readline

H, W = map(int, input().split())
board = [[[0,1][a == "#"] for a in input()] for i in range(H)]
Y = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        a = []
        if j == 0:
            pass
        else:
            if board[i][j-1] == False and board[i][j] == True:
                a.append(Y[i][j-1] + 1)
            else:
                a.append(Y[i][j-1])
        if i == 0:
            pass
        else:
            if board[i-1][j] == False and board[i][j] == True:
                a.append(Y[i-1][j] + 1)
            else:
                a.append(Y[i-1][j])
        if i + j == 0:
            if board[i][j]:
                a.append(1)
            else:
                continue
        Y[i][j] = min(a)


print(Y[H-1][W-1])
