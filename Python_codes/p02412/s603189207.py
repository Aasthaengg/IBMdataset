while True:
	n,x = map(int,raw_input().split(" "))
	c = 0
	if n == 0 and x == 0:
		break
	for i in range(1,n-1):
		for j in range(i+1,n):
			for h in range(j+1,n+1):
				if i + j + h == x:
					c += 1
	print c 