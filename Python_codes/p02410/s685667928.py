nm = input().split()
n = int(nm[0])
m = int(nm[1])

matrix = []

for i in range(n):
    row = []
    A = input().split()
    for a in A:
        row.append(int(a))

    matrix.append(row)

column = []
for i in range(m):
    column.append(int(input()))

for i in range(n):
    sum_list = []
    for j in range(m):
        sum_list.append(column[j]*matrix[i][j])
    print(sum(sum_list))