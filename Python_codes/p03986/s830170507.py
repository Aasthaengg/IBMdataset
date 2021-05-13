x = input()

stack = []

for c in x:
    if len(stack) == 0:
        stack.append(c)
    elif c == "T" and stack[-1] == "S":
        stack.pop(-1)
    else:
        stack.append(c)

print(len(stack))
