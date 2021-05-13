s = input()
l = 0
r = len(s)-1
res = 0
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x' and s[r] != 'x':
        res += 1
        l += 1
    elif s[l] != 'x' and s[r] == 'x':
        res += 1
        r -= 1
    elif s[l] != s[r] and s[l] != 'x' and s[r] != 'x':
        print(-1)
        exit()
print(res)