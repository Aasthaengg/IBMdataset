n, m, l = [int(i) for i in input().split()]

matrix_A = [list(map(int, input().split())) for i in range(n)]
matrix_B = [list(map(int, input().split())) for i in range(m)]
output_matrix = [[0 for i in range(l)] for j in range(n)]
for i in range(m):
    for j in range(l):
        for k in range(n):
            output_matrix[k][j] += matrix_A[k][i] * matrix_B[i][j]

for  tmp_list in output_matrix:
    print(" ".join(map(str, tmp_list)))