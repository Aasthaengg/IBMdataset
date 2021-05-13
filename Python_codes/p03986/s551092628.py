X = input()
stack = []
for x in X:
    if stack and stack[-1] == "S" and x == "T":
        stack.pop()
    else:
        stack.append(x)
print(len(stack))
