while True:
	try:
		y,x = map(int,input().split(" "))
		if y == 0 and x == 0:
			break
		for i in range(y):
			for j in range(x):
				if j == 0 or i == 0 or j == x-1 or i == y-1:
					print("#",end="")
				else:
					print(".",end="")
			print()
		print()
	except:
		break