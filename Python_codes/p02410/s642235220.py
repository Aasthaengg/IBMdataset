n, m = map(int, input().split())
matrix = []
lines = []
c_ele = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for j in range(m):
    lines.append(int(input()))

for k in range(n):
    sum = 0
    for l in range(m):
        sum += matrix[k][l] * lines[l]
    c_ele.append(sum)

for p in c_ele:
    print(p)

