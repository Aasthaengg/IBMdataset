def resolve():
	r = int(input())
	if r < 1200:
		return print('ABC')
	if r < 2800:
		return print('ARC')
	else:
		return print('AGC')
resolve()