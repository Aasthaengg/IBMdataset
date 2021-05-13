S = input()

flag = True
ans = ""
for s in S:
    if flag:
        ans += s
    flag = not flag
print(ans)
