S = input()
stack_0 = []
stack_1 = []

for s in S:
    if s == "0":
        if stack_1:
            stack_1.pop()
        else:
            stack_0.append(s)
    else:
        if stack_0:
            stack_0.pop()
        else:
            stack_1.append(s)

print(len(S) - len(stack_0) - len(stack_1))
