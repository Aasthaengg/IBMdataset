s = input()

n = len(s)
i = 0
ans = 1
pre = None
while i < n-1:
    if pre is None:
        pre = s[i]
    if pre == s[i+1]:
        pre = s[i+1:i+3]
        i += 2
    else:
        pre = s[i+1:i+2]
        i += 1
    if i < n:
        ans += 1


print(ans)
