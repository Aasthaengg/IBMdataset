s = input()

ans = 1
tmp = ''
bs = s[0]
for i in range(1, len(s)):
    tmp += s[i]
    if bs != tmp:
        ans += 1
        bs = tmp
        tmp = ''
print(ans)
