while True:
	s = str(input())
	if s == '-': break
	
	h = 0
	m = int(input())
	for i in range(m):
		h += int(input())
	h = h % len(s)
	print((s + s)[h:h+len(s)])

