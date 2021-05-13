import math
def resolve():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	i = a.index(min(a)) + 1
	if k - 1 > i:
		v = max(0, math.ceil((n - k - 2) / (k - 1))) + 1
	else:
		v = math.ceil(i / (k - 1)) + math.ceil((n - i - 1) / (k - 1))
	print(v)
resolve()