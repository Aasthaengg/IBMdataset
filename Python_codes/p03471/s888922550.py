N, Y = map(int, input().split())
x, y, z = -1, -1, -1

for i in range(N + 1):
	for j in range(N + 1 - i):
		k = (Y - i * 10000 - j * 5000) / 1000
		if k == N - i - j:
			x, y = i, j
			z = int(k)
			break
	else:
		continue
	break

print(x, y, z)