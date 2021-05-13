s = input()

ans = 10**13
for si in s:
    t = s
    for j in range(len(t)):
        tt = ''
        if len(set(t)) == 1:
            ans = min(ans, j)
            break
        for k in range(len(s)-j-1):
            if t[k] == si or t[k+1] == si:
                tt += si
            else:
                tt += '*'
        t = tt

print(ans)
