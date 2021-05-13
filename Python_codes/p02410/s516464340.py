n, m = [int(x) for x in input().split()]
matrix = []
for num in range(n):
    matrix.append([int(y) for y in input().split()])
colum = []
for num in range(m):
    colum.append(int(input()))
for i in range(n):
    a = 0
    for j in range(m):
        product = matrix[i][j] * colum[j]
        a += product
    print(a)