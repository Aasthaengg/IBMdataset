H, W = map(int, input().split())
arr = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == '#':
            flg =False
            if i-1>=0:
                if arr[i-1][j] == '#':
                    flg = True
            if j-1>=0:
                if arr[i][j-1] == '#':
                    flg = True
            if i+1<H:
                if arr[i+1][j] == '#':
                    flg = True
            if j+1<W:
                if arr[i][j+1] == '#':
                    flg = True
            if flg == False:
                print('No')
                exit()

print('Yes')


