from collections import deque

X = input()
n = len(X) # even

stack = deque([])

for char in X:
	if char == 'S':
		stack.append(char)
	elif char == 'T' and len(stack) == 0:
		stack.append('T')
	elif char == 'T' and stack[-1] == 'S':
		stack.pop()
	elif char == 'T' and stack[-1] == 'T':
		stack.append('T')

print(len(stack))