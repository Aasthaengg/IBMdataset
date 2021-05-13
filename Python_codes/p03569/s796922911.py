s = input()
n = len(s)

sr = s.replace("x", "")

if sr != "".join(reversed(sr)):
    print(-1)
else:
    ans = 0
    l = 0
    r = -1
    while l - r < n:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        elif s[l] == "x" and s[r] != "x":
            ans += 1
            l += 1
        elif s[l] != "x" and s[r] == "x":
            ans += 1
            r -= 1
        
    print(ans)
