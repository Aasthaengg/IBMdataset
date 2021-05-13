C = [list(map(int, input().split())) for _ in range(3)]
for i in range(2):
    for j in range(2):
        if C[i+1][j] - C[i][j] != C[i+1][j+1] - C[i][j+1]:
            print('No')
            exit()
print('Yes')