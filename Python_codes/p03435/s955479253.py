C = [list(map(int, input().split())) for _ in range(3)]

D = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        D[i][j] = C[i][j] - C[i][j-1]

if D[0] == D[1] == D[2]:
    print("Yes")
else:
    print("No")