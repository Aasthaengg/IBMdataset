s = input()
t = s.replace("x", "")

flag = 1
for i in range(len(t)):
    if t[i] != t[~i]:
        flag = 0

if flag == 0:
    print(-1)
else:
    ans = 0
    t = s[::-1]
    c = 0
    for i in range(len(s)):
        if c >= len(t):
            if s[i] == "x":
                ans += 1
            continue
        if t[c] == s[i]:
            c += 1
            continue
        else:
            if s[i] == "x":
                ans += 1
                continue
            else:
                while t[c] == "x":
                    ans += 1
                    c += 1
                else:
                    c += 1
    ans += len(t) - c
    print(ans//2)
