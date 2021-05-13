def draw(h,w):
	t = "#." * 150
	s = t[0:w]
	k = t[1:w+1]
	for i in range(0,h/2):
		print s
		print k
	if h%2==1:
		print s
	print

if __name__ == "__main__":
	while True:
		h,w = map(int, raw_input().split())
		if h==0 and w==0:
			break
		else:
			draw(h,w)