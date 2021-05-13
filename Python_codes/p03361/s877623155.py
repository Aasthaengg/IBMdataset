H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
for i in range(H):
    for j in range(W):
        safe = False
        s = S[i][j]
        if s == '#':
            if i != 0 and S[i-1][j] == '#': safe = True
            if j != 0 and S[i][j-1] == '#': safe = True
            if j != W-1 and S[i][j+1] == '#': safe = True
            if i != H-1 and S[i+1][j] == '#': safe = True
            if not safe:
                print('No')
                exit()
print('Yes')