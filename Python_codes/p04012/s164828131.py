def test():
	s = list(input())
	for w in s:
		if s.count(w)%2!=0:
			print('No')
			return
	print('Yes')
test()