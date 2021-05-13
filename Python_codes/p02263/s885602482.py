rp = [ele for ele in input().split()]
op = ['+','-','*']
stack = []
for ele in rp:
	if ele not in op:
		# ele is number
		stack.append(eval(ele))
	else:
		# ele is operator
		num_2 = stack.pop()
		num_1 = stack.pop()
		if ele == '+':
			stack.append(num_1 + num_2)
		elif ele == '-':
			stack.append(num_1 - num_2)
		else:
			# ele == '*'
			stack.append(num_1 * num_2)
print(stack[0])