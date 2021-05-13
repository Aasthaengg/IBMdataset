while 1:
	n, x = map(int, raw_input().split())
	if n == 0 and x == 0:
		break
	a = [int(m) for m in range(1, n+1)]
	N = 0
	for k in range(2, n):
		for j in range(1, k):
			for i in range(j):
				if a[i]+a[j]+a[k] == x:
					N += 1
				else:
					pass
	print N