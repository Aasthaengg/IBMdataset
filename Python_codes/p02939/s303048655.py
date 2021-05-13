s = list(input())
i = len(s)
ans = 0
while i >= 3:
    if s[i-1] != s[i-2]:
        i -= 1
        ans += 1
    else:
        i -= 3
        ans += 2
if i <= 1:
    print(ans+i)
else:
    if s[i-1] != s[i-2]:
        print(ans+2)
    else:
        print(ans+1)
