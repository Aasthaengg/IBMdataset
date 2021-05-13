s = input()

ans = 1
t = s[0]
i = 1

while i < len(s)-1:
    if len(t) == 2:
        t = s[i]
        i += 1
    elif t == s[i]:
        t = s[i:i+2]
        i += 2
    else:
        t = s[i]
        i += 1
    ans += 1

if i == len(s)-1 and t != s[-1]:
    print(ans + 1)
else:
    print(ans)