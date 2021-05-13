def resolve():
	n = int(input())
	for i in range(100):
		for j in range(100):
			if n == 4*i + 7*j:
				print('Yes')
				return
	print('No')
resolve()