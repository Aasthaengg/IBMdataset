stack = []

for s in input().split():
    if s == '+':
        stack.append(stack.pop() + stack.pop())
    elif s == '-':
        stack.append(-stack.pop() + stack.pop())
    elif s == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(s))
print(stack[0])