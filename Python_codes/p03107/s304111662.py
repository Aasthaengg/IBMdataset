s = input()

stack = [s[0]]
ans = 0
for i in range(1, len(s)):
    if len(stack) == 0:
        stack.append(s[i])
        continue
    if s[i] == "0":
        if stack[-1] == "1":
            del stack[-1]
            ans += 2
        else:
            stack.append("0")
    else:
        if stack[-1] == "0":
            del stack[-1]
            ans += 2
        else:
            stack.append("1")

print(ans)