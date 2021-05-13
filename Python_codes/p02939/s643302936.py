s = input()

l = 0
ans = 0
pre = ''
for r in range(len(s)):
    if pre != s[l:r+1]:
        pre = s[l:r+1]
        l = r+1
        ans += 1
print(ans)