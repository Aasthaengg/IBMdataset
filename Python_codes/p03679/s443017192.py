def resolve():
	x, a, b = map(int, input().split())
	if b - a > x:
		print('dangerous')
	elif a >= b:
		print('delicious')
	else:
		print('safe')
resolve()