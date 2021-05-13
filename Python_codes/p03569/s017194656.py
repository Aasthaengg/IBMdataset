s = list(input())
ans = 0
l = 0
r = len(s)-1
while l < r:
    if s[l] != s[r]:
        if s[l] == "x":
            ans += 1
            r += 1
        elif s[r] == "x":
            ans += 1
            l -= 1
        else:
            print(-1)
            exit()
    l += 1
    r -= 1
print(ans)