A = input().split()
stack = []
for s in A:
    if s.isdigit():
        stack.append(int(s))
    else:
        stack.append(eval('{2}{1}{0}'.format(stack.pop(), s, stack.pop())))
print(stack[0])
