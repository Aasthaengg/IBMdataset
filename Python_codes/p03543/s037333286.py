def resolve():
	n = list(input())
	for i in range(2):
		if n[i] == n[i+1] == n[i+2]:
			print('Yes')
			return
	print('No')
resolve()