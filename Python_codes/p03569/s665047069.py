s = input()

ss = ""
cnt = 0
for e in s:
    if e == "x":
        cnt += 1
    else:
        ss += e

if ss == ss[::-1]:
    l = 0
    r = len(s) - 1
    ans = 0
    while r > l:
        if s[l] == s[r] == "x":
            l += 1
            r -= 1
        elif s[l] == "x":
            l += 1
            ans += 1
        elif s[r] == "x":
            r -= 1
            ans += 1
        else: # s[l] == s[r]
            l += 1
            r -= 1

else:
    ans = -1

print(ans)
