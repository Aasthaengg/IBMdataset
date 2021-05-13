while True:
	a = ""
	b = ""
	H, W = map(int, input().split())

	if H == 0 and W == 0 : break

	for i in range(W):
		if i % 2 == 0 : a = a + "#"
		else : a = a + "."
	for i in range(W):
		if i % 2 == 0 : b = b + "."
		else : b = b + "#"

	for j in range(H):
		if j % 2 == 0: print(a)
		else : print(b)

	print()