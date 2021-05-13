tmp = input().strip().split()
stack = []
for i in tmp:
    if i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '-':
        stack.append(-stack.pop() + stack.pop())
    elif i == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(i))

print (stack[0])