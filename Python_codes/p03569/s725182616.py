s = input()
ans = 0
while len(s) > 0:
    if s[0] == s[-1]:
        s = s[1:len(s)-1]
    elif s[0] == 'x':
        s += 'x'
        ans += 1
    elif s[-1] == 'x':
        s = 'x' + s
        ans += 1
    else:
        print(-1)
        exit()
print(ans)
