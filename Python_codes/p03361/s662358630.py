H,W = map(int,input().split())

HW = [list(input()) for i in range(H)]

def isPaintable(i, j):
    if i - 1 >=0 :
        if HW[i-1][j] == '#':
            return True
    if j - 1 >=0 :
        if HW[i][j-1] == '#':
            return True
    if i + 1 < H :
        if HW[i+1][j] == '#':
            return True
    if j + 1 < W :
        if HW[i][j+1] == '#':
            return True
    return False

isOk = True

for i in range(H):
    for j in range(W):
        if HW[i][j] == '#':
            if isPaintable(i,j):
                continue
            else:
                isOk = False
                break

if isOk:
    print('Yes')
else:
    print('No')


