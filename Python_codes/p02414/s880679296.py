n,m,l = map(int,input().split())
matrixL = [[0]*m for i in range(n)]
matrixR = [[0]*l for i in range(m)]
for row in range(n):
    matrixL[row] = [int(i) for i in input().split()]

for row in range(m):
    matrixR[row] = [int(i) for i in input().split()]
c = [[0] * l for i in range(n)]
for ansColumn in range(l):
    for row in range(n):
        for column in range(m):
            c[row][ansColumn] = c[row][ansColumn] + matrixL[row][column] * matrixR[column][ansColumn]
for row in range(n):
    for column in range(l):
        if column == l -1:
            print(c[row][column])
        else:
            print("%d " %c[row][column], end ="")
