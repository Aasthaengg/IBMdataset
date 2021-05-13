while True:
	H,W = list(map(int, input().split()))
	if (H == 0)and(W == 0):
		break
	else:
		for i in range(H):
			s = ""
			for j in range(W):
				s += "#"
			print(s)
		print("")