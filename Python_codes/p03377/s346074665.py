c, d, x = map(int, input().split())
if c > x:
	print('NO')
else:
	if x - c > d:
		print('NO')
	else:
		print('YES')