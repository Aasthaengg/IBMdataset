s = input()
ans = 0
a = 0
i = 0
while i < len(s):
    c = s[i]
    if c == 'A':
        a += 1
    elif c == 'B':
        i += 1
        if i >= len(s):
            break
        c = s[i]
        if c == 'C':
            ans += a
        elif c == 'A':
            a = 1
        else:
            a = 0
    elif c == 'C':
        a = 0
    i += 1
print(ans)
