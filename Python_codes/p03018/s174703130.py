s = input()

aaa = 0
ans = 0
i = 0
while i < len(s) - 1:
    if s[i] == 'A':
        aaa += 1
    elif s[i:i+2] == 'BC':
        ans += aaa
        i += 1
    else:
        aaa = 0
    i += 1
print(ans)
