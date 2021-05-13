H,W = map(int,input().split())
pict = [input() for i in range(H)]
for i in range(H):
    for j in range(W):
        if pict[i][j] == '#':
            flag = False
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<H and 0<=y<W and pict[x][y]=='#':
                    flag = True
                    break
            if flag == False:
                print('No')
                exit(0)
print('Yes')