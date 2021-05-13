c = [list(map(int,input().split())) for i in range(3)]
b = [c[0][0] - 0,c[0][1] - 0,c[0][2] - 0]
a = [c[0][0] - b[0],c[1][0] - b[0],c[2][0] - b[0]]

for i in range(3):
    for j in range(3):
        if a[i] + b[j] != c[i][j]:
            print('No')
            exit(0)

print('Yes')