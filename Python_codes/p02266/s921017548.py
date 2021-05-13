s = input()
stack = []
stack1 = []
tot = 0
rs = []
for i in range(len(s)):
    if s[i] == '\\':
        stack.append(i)
    elif s[i] == '/':
        if len(stack) > 0:
            tmp = i - stack[-1]
            tot += tmp
            while len(stack1) > 0 and stack1[-1][0] > stack[-1]:
                tmp += stack1[-1][1]
                stack1.pop()
            stack1.append((stack[-1], tmp))
            stack.pop()
print(tot)
print(len(stack1), *(y for x,y in stack1))
