s = input()
ss = s.replace("x", "")
ssr = ss[::-1]
if  ss != ssr:
    print(-1)
else:
    l = 0
    r = len(s) - 1
    cnt = 0
    while l < r:
        if s[l] == s[r]:
            r -= 1
            l += 1
        elif s[l] == "x":
            cnt += 1
            l += 1
        elif s[r] == "x":
            cnt += 1
            r -= 1
    print(cnt)