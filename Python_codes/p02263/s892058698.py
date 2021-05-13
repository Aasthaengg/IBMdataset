a = input()
a = a.split(' ')
stack = []
for i in a:
    if i == '+' or i == '-' or i == '*':
        s = int(stack.pop())
        t = int(stack.pop())
        if i == '+':
            u = t + s
        if i == '-':
            u = t - s
        if i == '*':
            u = t * s
        stack.append(u)
    else:
        stack.append(i)

print(stack.pop())