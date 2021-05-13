s = input()

i = 0
ans = 0
while i < len(s)-1:
    # print(i, s[i], s[i+1], ans)
    if s[i] != s[i+1]:
        i += 1
        ans += 1
    else:
        if i == len(s)-2:
            i += 3
            ans += 1
        else:
            i += 3
            ans += 2
if i == len(s)-1:
    ans += 1
print(ans)
