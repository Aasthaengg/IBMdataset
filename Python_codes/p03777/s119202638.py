a,b = raw_input().split()
if a == 'H':
	print b
else:
	h = {'H':'D', 'D':'H'}
	print h[b]