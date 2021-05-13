x = list(map(lambda k : int(k),input().split(" ")))
if x[4] <= x[2] <= x[0]-x[4] and x[4] <= x[3] <= x[1] - x[4]:
	print("Yes")
else:
	print("No")