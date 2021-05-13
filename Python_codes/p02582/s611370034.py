s = input()
ans = 0
flag = 0
temp = 0
for i in range(len(s)):
    if s[i] == 'R':
        flag = 1
    else:
        flag = 0
    if flag:
        temp += 1
    else:
        temp = 0
    ans = max(ans, temp)

print(ans)
