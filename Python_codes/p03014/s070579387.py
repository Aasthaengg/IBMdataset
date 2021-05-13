import collections
n,m = map(int, raw_input().split(' '))
matrix = [list(raw_input()) for _ in range(n)]
dpleft = [[0 for j in range(m)] for i in range(n)]
dpright = [[0 for j in range(m)] for i in range(n)]
dpup = [[0 for j in range(m)] for i in range(n)]
dpdown = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
	cumul = 0
	for j in range(m):
		if matrix[i][j] == '#':
			cumul = 0
		else:
			dpleft[i][j] = cumul
			cumul +=1

	cumul = 0
	for j in range(m-1,-1,-1):
		if matrix[i][j] == '#':
			cumul = 0
		else:
			dpright[i][j] = cumul
			cumul +=1

for j in range(m):
	cumul = 0
	for i in range(n):
		if matrix[i][j] == '#':
			cumul = 0
		else:
			dpup[i][j] = cumul
			cumul +=1

	cumul = 0
	for i in range(n-1,-1,-1):
		if matrix[i][j] == '#':
			cumul = 0
		else:
			dpdown[i][j] = cumul
			cumul +=1
r = 0
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j] != '#':
			r = max(r, 1 + dpleft[i][j] + dpright[i][j] + dpdown[i][j] + dpup[i][j])

print r