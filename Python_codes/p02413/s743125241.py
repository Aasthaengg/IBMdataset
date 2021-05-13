# coding: utf-8

row,col = map(int, input().split())

cells = []

for r in range(row):
    temp_col = list(map(int, input().split()))
    temp_col.append(sum(temp_col))
    cells.append(temp_col)

cells.append([0] * (col + 1))
for c in range(col + 1):
    for r in range(row):
        cells[row][c] += cells[r][c]

for r in range(row+1):
    print(' '.join(map(str, cells[r])))