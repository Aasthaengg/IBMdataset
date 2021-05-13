s = input()

s = s.replace('BC', 'V')

ans = 0
cnt = 0
flag = False

for i in range(len(s)):
    if s[i] == 'A':
        flag = True
        cnt += 1
    elif flag and s[i] == 'V':
        ans += cnt
    else:
        flag = False
        cnt = 0

print(ans)
