s = input()
ans = ''
for i in range(3):
    if s[i] == '1':
        ans += '9'
    elif s[i] == '9':
        ans += '1'
    else:
        ans += s[i]
print(int(ans))
