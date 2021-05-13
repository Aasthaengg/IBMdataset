i, j = map(int, input().split())
a = []
b = []
result = []
for _ in range(i):
	a.append(list(map(int, input().split())))
for _ in range(j):
	b.append(int(input()))
for x in range(i):
	sum = 0
	for y in range(j):
		sum += a[x][y]*b[y]
	result.append(sum)
print (*result, sep="\n")