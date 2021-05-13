import sys

n, m = map(int, input().split())

matrix = [[0 for x in range(m + 1)] for y in range(n + 1)]

for i in range(n):
	arr = list(map(int, input().split()))
	for j in range(m):
		matrix[i][j] = arr[j]
		
for i in range(n):
	sum = 0
	for j in range(m):
		sum += matrix[i][j]
	matrix[i][m] = sum

for i in range(m + 1):
	sum = 0
	for j in range(n):
		sum += matrix[j][i]
	matrix[n][i] = sum
	
for i in range(n + 1):
	for j in range(m + 1):
		sys.stdout.write(str(matrix[i][j]))
		if j != m:
			sys.stdout.write(' ')
	print()

