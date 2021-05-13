def resolve():
	s = [input() for _ in range(2)]
	if s[0] == s[1][::-1]:
		print('YES')
	else:
		print('NO')
resolve()