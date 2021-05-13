def resolve():
	a, b, c, d = map(int, input().split())
	indir = abs(a - b) <= d and abs(b-c) <= d
	dir = abs(a-c) <= d
	if dir or indir:
		print('Yes')
	else:
		print('No')
resolve()