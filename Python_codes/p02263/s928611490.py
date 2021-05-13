command = raw_input().split(" ")
stack = []

for i in command:
    if i == "+":
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a + b)
    elif i == "-":
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a - b)
    elif i == "*":
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a * b)
    elif i == "/":
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a / b)
    else:
        stack.append(i)

print(stack.pop())