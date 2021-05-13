def calc(a, n, k):
	if n == 1:
		return min(a*2, a+k)
	t = calc(a, n-1, k)
	return min(t*2, t+k)

def resolve():
	n, k = [int(input()) for _ in range(2)]
	print(calc(1, n, k))
resolve()