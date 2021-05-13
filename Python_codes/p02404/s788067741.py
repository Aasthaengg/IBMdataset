while 1:
	H , W = map(int , raw_input().split())
	if H == 0 and W == 0:
		break
	print "#" * W
	for h in range(0,H-2):
		s = "#"
		for l in range(0,W-2):
			s += "."
		s += "#"
		print s

	print "#" * W
	print 