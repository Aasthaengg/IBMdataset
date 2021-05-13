
data = input().split()
n = len(data)

stack=[]

for i in data:
    if i == "+":
        x1 = int(stack.pop())
        x2 = int(stack.pop())
        stack.append(x1+x2)
    elif i == "-":
        x2 = int(stack.pop())
        x1 = int(stack.pop())
        stack.append(x1-x2)
    elif i == "*":
        x2 = int(stack.pop())
        x1 = int(stack.pop())
        stack.append(x1*x2)
    elif i == "/":
        x2 = int(stack.pop())
        x1 = int(stack.pop())
        stack.append(x1-x2)
    else:
        stack.append(int(i))
print(stack[0])