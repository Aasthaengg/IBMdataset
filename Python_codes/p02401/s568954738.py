while 1:
	input_data = [i for i in input().split()]
	if input_data[1] == '?':
		break;
	a = int(input_data[0])
	op = input_data[1]
	b = int(input_data[2])
	if op == '+':
		print(a+b)
	elif op == '-':
		print(a-b)
	elif op == '*':
		print(a*b)
	elif op == '/':
		print(int(a/b))