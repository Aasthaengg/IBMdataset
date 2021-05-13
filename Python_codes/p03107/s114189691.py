S = input()
stack = []

cnt = 0
for s in S:
    if len(stack) == 0:
        stack.append(s)
    elif len(stack) > 0 and stack[-1] != s:
        stack.pop()
        cnt += 2
    else:
        stack.append(s)

print(cnt)