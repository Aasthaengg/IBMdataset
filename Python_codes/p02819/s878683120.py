x = int(input())

if x == 2:
	print(2)
else:
	while True:
		for i in range(2,x):
			if x % i == 0:
				break
			if x - 1 == i:
				print(x)
				exit()
		x += 1