expression = input().split()
stack = []
for i in range(len(expression)):
	if expression[i] == '+':
		a = stack.pop()
		b = stack.pop()
		stack.append(a+b)
	elif expression[i] == '-':
		a = stack.pop()
		b = stack.pop()
		stack.append(b-a)
	elif expression[i] == '*':
		a = stack.pop()
		b = stack.pop()
		stack.append(a*b)
	else:
		stack.append(int(expression[i]))
print(str(stack.pop()))
