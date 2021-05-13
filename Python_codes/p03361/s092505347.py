H, W = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(1,H-1):
    for j in range(1,W-1):
        if S[i][j] == '#':
            if S[i+1][j] == '#' or S[i][j+1] == '#' or S[i-1][j] == '#' or S[i][j-1] == '#':
                continue
            else:
                print('No')
                exit()
print('Yes')
