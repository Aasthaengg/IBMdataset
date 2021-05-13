s = input()
key = s[0]
temp = ''
ans = 1
for i in range(1,len(s)):
    temp += s[i]
    if key != temp:
        ans += 1
        key = temp
        temp = ''


print(ans)
