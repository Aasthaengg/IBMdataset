x, y, z = map(int, input().split())
matrix1 = list()
matrix2 = list()
ans = list()
for i in range(x):
    matrix1.append(list(map(int, input().split())))
for j in range(y):
    matrix2.append(list(map(int, input().split())))
for i in range(x):
    row = list()
    for j in range(z):
        term = 0
        for k in range(y):
            term += matrix1[i][k]*matrix2[k][j] 
        row.append(term)
    ans.append(row)
for i in range(x):
    print (' '.join(map(str, ans[i])))
