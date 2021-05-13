ope = {"+": lambda a, b: a + b, "-": lambda a, b: b - a, "*": lambda a, b: a * b, "/": lambda a, b: a / b}
stack =[]

for i in input().split():
    if i in ope:
        stack.append(ope[i](stack.pop(),stack.pop()))
    else:
        stack.append(int(i))

print(stack[0])