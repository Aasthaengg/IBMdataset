n, m = [int(_) for _ in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(_) for _ in input().split()])
vector = []
for i in range(m):
    vector.append(int(input()))

for row in matrix:
    c = 0
    for i in range(m):
        c += row[i] * vector[i]
    print(c)
