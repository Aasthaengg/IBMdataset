data = list(map(int, input().split()))
mat1 = [[0 for j in range(data[1])] for i in range(data[0])]
mat2 = [[0 for j in range(data[2])] for i in range(data[1])]
mat3 = [[0 for j in range(data[2])] for i in range(data[0])]
for i in range(data[0]):
    row = list(map(int, input().split()))
    for j in range(data[1]):
        mat1[i][j] = row[j]
for i in range(data[1]):
    row = list(map(int, input().split()))
    for j in range(data[2]):
        mat2[i][j] = row[j]
for i in range(data[0]):
    for j in range(data[2]):
        elem = 0
        for k in range(data[1]):
            elem += mat1[i][k] * mat2[k][j]
        mat3[i][j] = elem
for i in range(len(mat3)):
    str_mat3 = list(map(str, mat3[i]))
    print(" ".join(str_mat3))

