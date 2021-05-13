a,b = map(int,input().split())

socket = 1 
number = 0

if b == 1:
	print(0)
else:
	while True:
		number += 1
		socket = socket - 1 + a
		if socket >= b:
			print (number)
			break