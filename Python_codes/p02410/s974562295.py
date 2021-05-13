n, m = map(int, input().split())

Mat = []

for i in range(n):
	row = list(map(int, input().split()))
	Mat.append(row)

b = []

for j in range(m):
	b.append(int(input()))

c = [0 for k in range(n)]

for l in range(n):
	for l2 in range(m):
		c[l] += (Mat[l][l2] * b[l2])
	print(c[l])