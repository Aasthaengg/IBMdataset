N, Y = map(int, input().split())

out = '-1 -1 -1'
for x in range(N + 1):
	for y in range(N + 1 - x):
		z = N - x - y
		total = 10000 * x + 5000 * y + 1000 * z
		if total == Y:
			out = '{} {} {}'.format(x, y, z)
			break
print(out)
