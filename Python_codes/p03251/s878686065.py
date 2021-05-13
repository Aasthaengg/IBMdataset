def resolve():
	n, m, x, y = map(int, input().split())
	xp = list(map(int, input().split()))
	yp = list(map(int, input().split()))
	for i in range(-99, y+1):
		ok = True
		if i <= x or i > y:
			continue
		for cx in xp:
			if cx >= i:
				ok = False
				break
		for cy in yp:
			if cy < i:
				ok = False
				break
		if ok:
			print('No War')
			return
	print('War')
resolve()