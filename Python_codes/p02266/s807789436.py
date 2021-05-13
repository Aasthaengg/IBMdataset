l = input()
l += "_"
stack1 = []
stack2 = []
A = 0
for i in range(len(l)):
    if l[i] == "\\":
        stack1.append(i)
    elif l[i] == "/" and stack1:
        b = stack1.pop()
        a = i - b
        A += a
        while stack2 and stack2[-1][0] > b:
            a += stack2.pop()[1]
        stack2.append([b, a])
print(A)
print(len(stack2), *(i[1] for i in stack2))
