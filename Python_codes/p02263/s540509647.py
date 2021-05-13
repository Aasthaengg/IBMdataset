a = input().split()

stack = []
for inp in a:
    if inp == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)
    elif inp == "-":
        x = stack.pop()
        y = stack.pop()
        stack.append(y-x)
    elif inp == "*":
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)
    else:
        stack.append(int(inp))

print(*stack)