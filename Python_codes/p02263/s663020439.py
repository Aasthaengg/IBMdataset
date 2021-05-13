line = input().split()
stack = []
for i in range(len(line)):
    obj = line[i]
    if obj.isnumeric():
        stack.append(obj)
    else:
        b = int(stack.pop(-1))
        a = int(stack.pop(-1))
        if obj == '+':
            stack.append(a+b)
        elif obj == '-':
            stack.append(a-b)
        else:
            stack.append(a*b)
print(stack[0])