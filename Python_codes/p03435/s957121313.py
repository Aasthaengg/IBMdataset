C = [list(map(int,input().split())) for _ in range(3)]
D1 = [[] for _ in range(3)]
D2 = [[] for _ in range(3)]
for i in range(3):
    for j in range(2):
        D1[i].append(C[i][j] - C[i][j + 1])
for j in range(3):
    for i in range(2):
        D2[j].append(C[i][j] - C[i + 1][j])
print('Yes' if D1[0] == D1[1] == D1[2] and D2[0] == D2[1] == D2[2] else 'No')