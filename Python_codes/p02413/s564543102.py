row, col = map(int, raw_input().split())

mat = []
for i in range(row):
    line = map(int, raw_input().split())
    mat.append(line + [sum(line)])

row2 = [0 for i in range(col+1)]
for i in range(col+1):
    for j in range(row):
        row2[i] += mat[j][i]
mat.append(row2)
for i in mat:
    print " ".join(map(str,i))