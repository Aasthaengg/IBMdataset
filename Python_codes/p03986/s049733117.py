def resolve():
    X = input()
    stack = []
    for s in X:
        if not stack:
            stack.append(s)
            continue
        if s == 'T' and stack[-1] == 'S':
            stack.pop()
        else:
            stack.append(s)
    print(len(stack))

resolve()