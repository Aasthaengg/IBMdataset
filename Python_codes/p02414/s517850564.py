n, m, l = map(int,input().split())

A = [[0 for i in range(m)] for j in range(n)]
B = [[0 for i in range(l)] for j in range(m)]
C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
	A[i] = input().split()
for i in range (m):
	B[i] = input().split()

for i in range(n):
	for j in range(l):
		for k in range(m):
			C[i][j] += int(A[i][k]) * int(B[k][j])
			
[print(*row) for row in C]