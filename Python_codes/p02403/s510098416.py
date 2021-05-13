while 1:
	n = input().split()
	H = int(n[0])
	W = int(n[1])
	if H == 0 and W == 0:
		break
	for i in range(0,H):
		for j in range(0,W):
			print("#",end="")
		print("")
	print("")