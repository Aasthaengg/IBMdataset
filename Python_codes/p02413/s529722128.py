r, c = map(int, input().split())
matrix = [[int(n) for n in input().split()] for row in range(r)]

for i, row in enumerate(matrix):
    matrix[i].append(sum(row))

end = [0 for _ in range(c+1)]
for i in range(c+1):
    for row in matrix:
        end[i] += row[i]

matrix.append(end)

for row in matrix:
    row = map(str, row)
    print(" ".join(row))
