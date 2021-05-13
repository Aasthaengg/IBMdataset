n, m, l = map(int, input().split())

def get_matrix(n):
	matrix = []
	for i in range(n):
		matrix.append(list(map(int, input().split())))
	return matrix

A = get_matrix(n)
B = get_matrix(m)

for i in range(n):
	for j in range(l):
		sum = 0
		for k in range(m):
			sum += A[i][k]*B[k][j]
		if j == l-1: print(sum)
		else: print(sum, end=' ')
