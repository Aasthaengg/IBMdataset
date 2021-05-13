s = input()

ans, cnta = 0, 0
for i in range(len(s)):
    if s[i] == 'A':
        cnta += 1
    elif s[i:i + 2] == 'BC':
        ans += cnta
    elif s[i - 1:i + 1] != 'BC':
        cnta = 0
print(ans)
