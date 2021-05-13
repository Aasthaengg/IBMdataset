stack = []
for l in raw_input():
	if len(stack) == 0 or stack[-1] != l: stack.append(l)
print len(stack) -1