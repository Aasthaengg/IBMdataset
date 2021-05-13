while True:
	h,w=map(int,input().split())
	if h==w==0:break
	for hh in range(h):
		print(('#' * w) if(hh==0 or hh==h-1)else('#' + '.' * (w - 2) + '#'))
	print()