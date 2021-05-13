while True:
	H,W = list(map(int, input().split()))
	if (H == 0) and (W == 0):
		break
	else:
		for n in range(0, H):
			s = ""
			for m in range(0, W):
				if (1 <= n and n <= (H-2)) and(1 <= m and m <= (W-2)):
					s += "."
				else :
					s += "#"
			print(s)
		print("")