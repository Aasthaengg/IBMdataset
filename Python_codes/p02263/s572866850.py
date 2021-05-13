a = list(map(str,input().split()))
stack = []

for x in a:
    if x == '+':
        stack.append(int(stack.pop()) + int(stack.pop()))
    elif x == '-':
        stack.append(-int(stack.pop()) + int(stack.pop()))
    elif x == '*':
         stack.append(int(stack.pop()) * int(stack.pop()))
    else:
        stack.append(x)
print(int(stack.pop()))
