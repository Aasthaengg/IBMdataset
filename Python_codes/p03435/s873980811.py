C = [list(map(int, input().split())) for _ in range(3)]

Dif_H = [[] for _ in range(3)]
Dif_V = [[] for _ in range(3)]

for i in range(3):
    Dif_H[i] = [C[i][0] - C[i][1], C[i][1] - C[i][2], C[i][2] - C[i][0]]
for i in range(3):
    Dif_V[i] = [C[0][i] - C[1][i], C[1][i] - C[2][i], C[2][i] - C[0][i]]

if Dif_H[0] == Dif_H[1] == Dif_H[2] and Dif_V[0] == Dif_V[1] == Dif_V[2]:
    print('Yes')
else:
    print('No')