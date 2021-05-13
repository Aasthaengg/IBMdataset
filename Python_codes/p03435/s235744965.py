cs = [list(map(int,input().split()))for _ in range(3)]
for i in range(2):
    yoko = abs(cs[0][i] - cs[0][i + 1])
    for j in range(1,3):
        if yoko - abs(cs[j][i] - cs[j][i + 1]) != 0:
            print('No')
            exit()

for i in range(2):
    tate = abs(cs[0+i][0] - cs[1+i][0])
    for j in range(1,3):
        if tate - abs(cs[i][j] - cs[i+1][j]) != 0:
            print('No')
            exit()
print('Yes')