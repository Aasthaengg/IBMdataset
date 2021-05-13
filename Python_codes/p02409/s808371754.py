num = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
b, f, r, v, v1, n, x, y, z  = 0, 0, 0, 0, 0, 0, 0, 0, 0
n = int(input())
for i in range(n):
	b, f, r, v = list(map(int, input().split()))
	num[b - 1][f - 1][r - 1] += v
for i in range(4):
	if y >= 1:
		z = 0
		y = 0
		x += 1
		print()
		print('####################')
	for i in range(3):
		if z >= 1:
			z = 0
			y += 1
			print('')
		for i in range(10):
			print('', num[x][y][z], end = '')
			z += 1
print()