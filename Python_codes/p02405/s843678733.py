x = []
s = ['','']
while 1:
	H,W = map(int, raw_input().split())
	if H == 0 and W == 0:
		break
	tmp = (W+1)/2
	s[0] = ('#.' * tmp)[:W]
	s[1] = ('.#' * tmp)[:W]
	
	for l in range(H):
		print s[l % 2]
	print 