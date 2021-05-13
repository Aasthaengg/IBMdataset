import sys

n, k = list(map(int, input().split()))

if k > (n - 1) * (n - 2) // 2:
	print(-1)
else:
	rest = (n - 1) * (n - 2) // 2 - k
	print((n - 1) + rest)
	for i in range(2, n + 1):
		print("1 " + str(i))

	for i in range(2, n + 1):
		for j in range(i + 1, n + 1):
			if rest == 0:
				sys.exit()
			print(str(i) + " " + str(j))
			rest -= 1
