while True:
	a = sorted(list(map(lambda x : int(x), input().split(" "))))
	if a[0] == 0 and a[1] == 0:
		break
	print("%d %d" % (a[0], a[1]))