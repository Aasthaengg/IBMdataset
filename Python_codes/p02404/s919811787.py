while True:	
	H,W = map(int, input().split())
	if H==0 and W==0: break
	for y in range(0,H):
		for x in range(0,W):
			if y==0 or y==H-1: print("#",end="")
			else:
				if x == 0 or x==W-1: print("#",end="")
				else: print(".",end="")
		print()
	print()
