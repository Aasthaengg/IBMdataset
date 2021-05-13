stack = []
for s in input().split():
    if s.isdigit():
        stack.append(s)
    else:
        y, x = (stack.pop() for _ in range(2))
        stack.append(str(eval(x + s + y)))
print(stack.pop())