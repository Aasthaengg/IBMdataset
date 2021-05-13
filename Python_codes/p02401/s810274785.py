while True:
	a,b,c = input().split()
	num_1 = int(a)
	num_2 = int(c)

	if b == '?':
		break
	elif b == '+':
		print(num_1 + num_2)
	elif b == '-':
		print(num_1 - num_2)
	elif b == '*':
		print(num_1 * num_2)
	else:
		print(num_1 // num_2)