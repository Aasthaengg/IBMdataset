s = input()
t = "".join([m for m in s if m != "x"])
u = t[::-1]
#print(t,u)
if t != u:
    print(-1)
    exit()
else:
    i = 0
    j = len(s)-1
    ans = 0
    while i <= j:
        if s[i] != s[j]:
            if s[i] == "x":
                ans += 1
                i += 1
            else:
                ans += 1
                j -= 1
        else:
            i += 1
            j -= 1
    print(ans)