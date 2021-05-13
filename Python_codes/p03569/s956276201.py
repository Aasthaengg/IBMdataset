s = input()
l = 0
r = len(s) - 1
ans = 0
while r > l:
    if s[r] == s[l]:
        l += 1
        r -= 1
    elif s[r] == "x":
        r -= 1
        ans += 1
    elif s[l] == "x":
        l += 1
        ans += 1
    else:
        ans = -1
        break
print(ans)