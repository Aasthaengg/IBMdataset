X = input()
stack = []
for c in X:
    if not stack:
        stack.append(c)
        continue
    if stack[-1] == "S" and c == "T":
        stack.pop()
    else:
        stack.append(c)
print(len(stack))
