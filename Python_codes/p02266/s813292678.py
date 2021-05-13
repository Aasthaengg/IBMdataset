s = input()
stack1 = []
stack2 = []
for i in range(len(s)):
    if s[i] == '\\':
        stack1.append(i)
    elif s[i] == '/' and stack1:
        j = stack1.pop()
        area = i-j
        while stack2:
            if stack2[-1][0] < j:
                break
            else:
                area += stack2.pop()[1]
        stack2.append((j,area))
ans = list(stack2[i][1] for i in range(len(stack2)))
print(sum(ans))
if ans:
    print(len(ans),' '.join(map(str,ans)))
else:
    print(0)
