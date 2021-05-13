x = input()
stack = []
for xx in x:
    if xx == "T":
        if len(stack) > 0:
            if stack[-1] == "S":
                stack.pop()
            else:
                stack.append(xx)
        else:
            stack.append(xx)
    else:
        stack.append(xx)

print(len(stack))

