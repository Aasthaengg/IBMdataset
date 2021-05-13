H, W = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(H):
    S[i] = list(S[i])
    
if (H == 1) and (W == 1):
    if S[0][0] == '.':
        S[0] = '0'
elif (H == 1) and (W != 1):
    for col in range(W):
        if S[0][col] == '#':
            continue
        if col == 0:
            S[0][col] = str([S[0][col+1]].count('#'))
        elif col == W - 1:
            S[0][col] = str([S[0][col-1]].count('#'))
        else:
            S[0][col] = str([S[0][col-1], S[0][col+1]].count('#'))
elif (H != 1) and (W == 1):
    for row in range(H):
        if S[row][0] == '#':
            continue
        if row == 0:
            S[row][0] = str([S[row+1][0]].count('#'))
        elif row == H - 1:
            S[row][0] = str([S[row-1][0]].count('#'))
        else:
            S[row][0] = str([S[row-1][0], S[row+1][0]].count('#'))
else:
    for row in range(H):
        for col in range(W):
            if S[row][col] == '#':
                continue
            if row == 0:
                if col == 0:
                    S[row][col] = str([S[row][col+1], S[row+1][col], S[row+1][col+1]].count('#'))
                elif col == W - 1:
                    S[row][col] = str([S[row][col-1], S[row+1][col-1], S[row+1][col]].count('#'))
                else:
                    S[row][col] = str([S[row][col-1], S[row][col+1], S[row+1][col-1],
                               S[row+1][col], S[row+1][col+1]].count('#'))
            elif row == H - 1:
                if col == 0:
                    S[row][col] = str([S[row-1][col], S[row-1][col+1], S[row][col+1]].count('#'))
                elif col == W - 1:
                    S[row][col] = str([S[row-1][col-1], S[row-1][col], S[row][col-1]].count('#'))
                else:
                    S[row][col] = str([S[row-1][col-1], S[row-1][col], S[row-1][col+1],
                                   S[row][col-1], S[row][col+1]].count('#'))
            else:
                if col == 0:
                    S[row][col] = str([S[row-1][col], S[row-1][col+1],
                                   S[row][col+1],
                                   S[row+1][col], S[row+1][col+1]].count('#'))
                elif col == W - 1:
                    S[row][col] = str([S[row-1][col-1], S[row-1][col],
                                   S[row][col-1], 
                                   S[row+1][col-1], S[row+1][col]].count('#'))
                else:
                    S[row][col] = str([S[row-1][col-1], S[row-1][col], S[row-1][col+1],
                                   S[row][col-1], S[row][col+1],
                                   S[row+1][col-1], S[row+1][col], S[row+1][col+1]].count('#'))
for i in range(len(S)):
    print(''.join(S[i]))  