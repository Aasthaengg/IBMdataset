inl = list(map(str, input().split()))

stack = []
for n in inl:
    if n == '+':
        stack.append(stack.pop() + stack.pop())
    elif n == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif n == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(n))
print(stack.pop())
