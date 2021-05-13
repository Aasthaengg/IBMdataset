s = input()

s = s.replace('BC','D')

a = 0
ans = 0

for i in range(len(s)):
    if s[i] == 'A':
        a += 1
    elif s[i] == 'D':
        if a != 0:
            ans += a
    else:
        a = 0

print(ans)