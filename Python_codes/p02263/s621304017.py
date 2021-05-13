line= input().split(" ")
op = ["+","-","*"]

stack = []

def push(i):
	stack.append(i)

def pop(i):
	return stack.pop(i)

for i in line:
	if i not in op:
		push(int(i))
	else:
		if i == "+":
			push(pop(-1) + pop(-1))
		elif i == "-":
			push(pop(-2) - pop(-1))
		elif i == "*":
			push(pop(-1) * pop(-1))

print(*stack)

