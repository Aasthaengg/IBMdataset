import re

data = input().split(' ')
stack = []
for w in data:
    if re.match(r'[0-9]', w):
        stack.append(w)
        # print(stack)
    else:
        r = stack.pop()
        l = stack.pop()
        stack.append(eval(str(l) + w + str(r)))
        # print(stack)

print(stack[0])