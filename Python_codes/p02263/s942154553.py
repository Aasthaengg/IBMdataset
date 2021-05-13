fig = input()
symbol = fig.split(' ')
stack = []

for i in symbol:
    try:
        stack.append(int(i))
    except ValueError:
       if i == "+": stack.append(stack.pop()+stack.pop())
       elif i == "-": stack.append(-(stack.pop()-stack.pop()))
       elif i == "*": stack.append(stack.pop()*stack.pop())

print(stack[0])