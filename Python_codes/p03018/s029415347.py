s = input()
cnt = 0
ans = 0
flag = False
for i in range(len(s) - 1):
    if flag:
        flag = False
        continue
    if s[i: i + 2] == 'BC':
        ans += cnt
        flag = True
    elif s[i] == 'A':
        cnt += 1
    else:
        cnt = 0
print(ans)