c = [0]*3
for i in range(3):
	c[i] = list(map(int,input().split()))
a = [0]*3
b = [0]*3
a[0] = 0
for j in range(3):
	b[j] = c[0][j] - a[0]
a[1] = c[1][0] - b[0]
a[2] = c[2][0] - b[0]
count = 0
for i in range(3):
	for j in range(3):
		if c[i][j] == a[i] + b[j]:
			count += 1
if count == 9:
	print('Yes')
else:
	print('No')