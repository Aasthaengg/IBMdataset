import sys

n,m,l = map(int, input().split())

a = [[0 for x in range(m)] for y in range(n)]
b = [[0 for x in range(l)] for y in range(m)]
c = [[0 for x in range(l)] for y in range(n)]

for i in range(n):
	arr = list(map(int, input().split()))
	for j in range(m):
		a[i][j] = arr[j]

for i in range(m):
	arr = list(map(int, input().split()))
	for j in range(l):
		b[i][j] = arr[j]

for i in range(n):
	for j in range(l):
		sum = 0
		for k in range(m):
			sum += a[i][k] * b[k][j]
		c[i][j] = sum
		
for i in range(n):
	for j in range(l):
		sys.stdout.write(str(c[i][j]))
		if j != l - 1:
			sys.stdout.write(' ')
	print()

