while 1:
	H, W = map(int, raw_input().split())
	if H == W == 0:
		break
	for h in range(H):
		if h % 2 == 0:
			if W % 2 == 0:
				print ("#."*(W//2))
			else:
				print ("#."*(W//2) + "#")
		else:
			if W % 2 == 0:
				print (".#"*(W//2))
			else:
				print (".#"*(W//2) + ".")
	print ""