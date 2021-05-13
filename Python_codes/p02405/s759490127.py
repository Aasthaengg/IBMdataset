while True:
	[H, W] = list(map(int, input().split()))

	if H == 0 and W == 0:
		break

	for i in range(H):
		for j in range(W):
			k = j
			if i % 2 == 0:
				k += 1

			if k % 2 == 0:
				print(".", end = "")
			else:
				print("#", end = "")

		print("")
	print("")