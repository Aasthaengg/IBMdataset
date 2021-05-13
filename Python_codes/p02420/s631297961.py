while 1:
	s = raw_input()
	if s == '-':
		break
	else:
		m = input()
		for _ in range(m):
			h = input()
			s = s[h:] + s[:h]
	print s