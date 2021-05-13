s = input()
ans = 0
tmp = ''
buf = ''

for i in range(len(s)):
    tmp += s[i]
    if tmp != buf:
        buf = tmp
        ans += 1
        tmp = ''

print(ans)
