s = input()
l = 0
r = len(s)-1
ans = 0
while l < r:
    while (s[l] == 'x' or s[r] == 'x') and l < r:
        if s[l] != s[r]:
            ans += 1
        if s[l] == 'x':
            l += 1
        if s[r] == 'x':
            r -= 1
    if s[l] != s[r]:
        break
    l += 1
    r -= 1
else:
    print(ans)
    exit()
print(-1)
