def resolve():
	n, a = [int(input()) for _ in range(2)]
	if n % 500 > a:
		print('No')
	else:
		print('Yes')
resolve()