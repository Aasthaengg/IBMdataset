notation = input().split()
stack = []
for s in notation:
    try:
        stack.append(int(s))
    except:
        n = 0
        if s == '+':
            n = stack[-2] + stack[-1]
        elif s == '-':
            n = stack[-2] - stack[-1]
        elif s == '*':
            n = stack[-2] * stack[-1]
        elif s == '/':
            n = stack[-2] / stack[-1]

        stack = stack[:-2] + [n]

assert(len(stack) == 1)
print(stack[0])

