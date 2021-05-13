data = list(map(int, input().split()))
row = data[0]+1
column = data[1]+1
table = [[0 for j in range(column)] for i in range(row)]
for i in range(row-1):
    data_in = list(map(int, input().split()))
    for j in range(column-1):
        table[i][j] = data_in[j]
for i in range(row):
    sum_row = 0
    for j in range(column):
        sum_row += table[i][j]
    table[i][column-1] = sum_row
for i in range(column):
    sum_column = 0
    for j in range(row):
        sum_column += table[j][i]
    table[row-1][i] = sum_column
for i in range(row):
    for j in range(column):
        if(j==column-1):
            print(str(table[i][j]))
        else:
            print("{0}".format(table[i][j]), end=" ")
