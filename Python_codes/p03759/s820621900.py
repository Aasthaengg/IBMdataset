a, b, c= map(int, open(0).read().split())
if b-a == c-b:
	print('YES')
else:
	print('NO')