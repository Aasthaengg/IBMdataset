A = list(map(str,input().split()))
stack = []
for item in A:
    if item != '+' and item != '-' and item != '*':
        stack.append(str(item))
    elif item == '+':
        v = int(stack[-2]) + int(stack[-1])
        del stack[-2]
        del stack[-1]
        stack.append(str(v))
    elif item == '-':
        v = int(stack[-2]) - int(stack[-1])
        del stack[-2]
        del stack[-1]
        stack.append(str(v))
    elif item == '*':
        v = int(stack[-2]) * int(stack[-1])
        del stack[-2]
        del stack[-1]
        stack.append(str(v))

print(stack[-1])

