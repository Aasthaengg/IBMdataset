n, m = [int(x) for x in input().split()]
s = input()
c = n
h = []
while(True):
	d = m
	while d > 0:
		if c - d >= 0:
			if s[c - d] == '0':break
		d -= 1
	if d == 0:
		print(-1)
		break
	c -= d
	h.append(str(d))
	if c == 0:
		h.reverse()
		print(' '.join(h))
		break