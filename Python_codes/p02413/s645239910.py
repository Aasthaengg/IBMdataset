r,c = list(map(int,input().split()))
matrix = []
for i in range(r):
	matrix.append(list(map(int,input().split())))
	matrix[i].append(sum(matrix[i]))
add_list = []
for j in range(c+1):
	num = 0
	for k in range(r):
		num += matrix[k][j]
	add_list.append(num)
matrix.append(add_list)

for i in range(r+1):
	out = ''
	for m in matrix[i]:
		out += str(m) + ' '
	print(out[:-1])