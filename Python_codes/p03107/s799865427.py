S = input()
stack = []
for s in S:
    if not stack:
        stack.append(s)
    else:
        if s == stack[-1]:
            stack.append(s)
        else:
            stack.pop()
print(len(S)-len(stack))