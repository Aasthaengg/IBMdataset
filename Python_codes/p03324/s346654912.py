def calc(n):
	if n % 100 != 0:
		return 0
	return calc(n/100) + 1

def resolve():
	d, n = map(int, input().split())
	n = n + calc(n)
	print(100**d*n)
resolve()