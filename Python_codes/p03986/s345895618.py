x = input()
stack = []
for s in x:
    if s == 'S':
        stack.append(s)
    else:
        if not stack:
            stack.append(s)
        elif stack[-1] == 'S':
            stack.pop()
        else:
            stack.append(s)
print(len(stack))
