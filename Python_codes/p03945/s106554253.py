s = input()
ans = 0
iro = ''

for i in range(len(s)):
    if i == 0:
        iro = s[0]
    elif iro != s[i]:
        ans += 1
        iro = s[i]

print(ans)
