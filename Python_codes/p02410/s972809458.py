a = []; b = []; c = []
n, m = map(int, input().split())

for i in range(n):
	row = map(int, input().split())
	a.append(list(row))

for j in range(m):
	col = int(input())
	b.append(col)

for k in range(n):
	temp = 0
	for l in range(m):
		temp += a[k][l] * b[l] 
	c.append(temp)

for ind in range(n):
	print(c[ind])