string = input()
stack = []
for c in string:
    if len(stack) == 0:
        stack.append(c)
        continue
    if stack[-1] + c == 'ST':
        stack.pop()
    else:
        stack.append(c)

print(len(stack))