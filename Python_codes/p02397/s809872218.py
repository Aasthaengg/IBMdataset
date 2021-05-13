while True:
	n,k = map(int, raw_input().split())
	if 0==n and 0==k:
		break
	if n > k:
		print k,n
	else:
		print n,k