c = [list(map(int, input().split())) for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                if c[i][j] + c[k][l] != c[i][l] + c[k][j]:
                    print('No')
                    exit()
print('Yes')
