import sys
(n, m) = [int(i) for i in sys.stdin.readline().split()]
matrix = []
for i in range(0, n):
    a_i = [int(j) for j in sys.stdin.readline().split()]
    matrix.append(a_i)
vector = []
for i in range(0, m):
    b_i = int(sys.stdin.readline())
    vector.append(b_i)

for i in range(0, n):
    c = 0
    for j in range(0, m):
        c += matrix[i][j] * vector[j]
    print(c)