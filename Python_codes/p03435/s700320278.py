c = [list(map(int,input().split())) for i in range(3)]
for i in range(2):
    if (c[i+1][0]-c[i][0]) == (c[i+1][1]-c[i][1]) == (c[i+1][2]-c[i][2]):
        continue
    else:
        print('No')
        exit(0)
for j in range(2):
    if (c[0][j+1]-c[0][j]) == (c[1][j+1]-c[1][j]) == (c[2][j+1]-c[2][j]):
        continue
    else:
        print('No')
        exit(0)
print('Yes')
