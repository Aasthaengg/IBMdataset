s = input()

s1 = s.replace('x', '')

if s1 != s1[::-1]:
    print(-1)
    exit()

l, r = 0, len(s)-1
ans = 0
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x':
        l += 1
        ans += 1
    elif s[r] == 'x':
        r -= 1
        ans += 1
print(ans)
