line = int(input())
for i in range(line):
	a,b,c = sorted([int(i) for i in input().split(' ')])

	if a**2 + b**2 == c**2:
		print('YES')
	else:
		print('NO')