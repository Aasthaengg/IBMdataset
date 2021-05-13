s = input()

i = 0
j = len(s)-1

ans = 0
while i < j:
    if s[i] == s[j]:
        i += 1
        j -= 1
    elif s[i] == "x":
        i += 1
        ans += 1
    elif s[j] == "x":
        j -= 1
        ans += 1
    else:
        break

if i >= j:
    print(ans)
else:
    print(-1)
