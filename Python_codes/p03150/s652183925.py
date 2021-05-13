s=input();ans='NO'
if s == 'keyence':
    ans = 'YES'
l = len(s)
if len(s) >= 8:
    i = 0
    while i < 8:
        s0 = s[:i]+s[i+(len(s)-7):]
        if s0 == 'keyence':
            ans = 'YES'
            break
        i += 1
print(ans)