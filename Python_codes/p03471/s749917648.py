N, Y = map(int, input().split())
Y //= 1000

for m in range(Y // 10, -1, -1):
	for g in range((Y - m * 10) // 5, -1, -1):
		if 10 * m + 5 * g + (N - m - g) == Y:
			print(m, g, N - m - g)
			exit()
print(-1, -1, -1)