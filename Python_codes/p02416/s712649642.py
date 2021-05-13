while True:
	x = int(input())
	if x == 0: break
	
	sum = 0
	while x is not 0:
		sum += x % 10
		x //= 10
	print(sum)
