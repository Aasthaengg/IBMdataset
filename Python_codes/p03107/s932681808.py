s = map(int, input())

ans = 0
stack = [2]
for e in s:
    if stack[-1] ^ e == 1:
        stack.pop()
        ans += 2
    else:
        stack.append(e)

print(ans)
