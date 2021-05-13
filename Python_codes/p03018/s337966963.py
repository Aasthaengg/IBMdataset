def test(s):

	res = 0
	aAdd = 0
	last = ''
	tmp = ''
	for i in xrange(len(s)):
		if tmp and tmp > i:
			continue
		if s[i] == 'A':
			aAdd += 1
		elif s[i:i+2] == 'BC':
			# print aAdd
			res = res + aAdd
			tmp = i + 2
		else:
			aAdd = 0
			last = s[i]


	return res
s=raw_input()
print test(s)