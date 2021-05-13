s = raw_input()
sentence = s.split(" ")
stack = []

for factor in sentence:
	if factor == "+":
		b = stack.pop()
		a = stack.pop()
		c = a + b
		stack.append(c)
	elif factor == "-":
		b = stack.pop()
		a = stack.pop()
		c = a - b
		stack.append(c)
	elif factor == "*":
		b = stack.pop()
		a = stack.pop()
		c = a * b
		stack.append(c)
	else:
		stack.append(int(factor))
print stack[0]