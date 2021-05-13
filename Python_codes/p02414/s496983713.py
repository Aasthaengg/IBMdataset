n,m,l = [int(i) for i in input().split()]
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
for i in range(n):
	a[i] = [int(j) for j in input().split()]
for i in range(m):
	b[i] = [int(j) for j in input().split()]
c = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
	for j in range(l):
		for k in range(m):
			c[i][j] += a[i][k] * b[k][j]
for i in range(n):
	for j in range(l-1):
		print(c[i][j],end=' ')
	print(c[i][l-1])