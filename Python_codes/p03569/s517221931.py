s = input()
t = s.replace('x', '')
if all(t[i] == t[len(t) - i - 1] for i in range(len(t) // 2)):
    l = 0
    r = len(s) - 1
    count = 0
    while r - l > 0:
        if s[l] != s[r]:
            count += 1
            if s[l] == 'x':
                l += 1
            if s[r] == 'x':
                r -= 1
        else:
            l += 1
            r -= 1
    print(count)
else:
    print(-1)
