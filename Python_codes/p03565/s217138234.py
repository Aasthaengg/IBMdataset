s = input()[::-1]
t = input()[::-1]
l = []
pre = 0

for i in range(len(s)):
    l.clear()
    cnt = 0
    pre = i
    while cnt < len(t) :
        if pre + cnt >= len(s):
            break
        if s[i] == t[cnt] or s[i] == "?":
            l.append(t[cnt])
            i += 1
            cnt += 1
        else:
            break
    else:
        ans = s[:pre] + "".join(l) + s[i:]
        ans = ans.replace("?", "a")
        ans = ans[::-1]
        print(ans)
        exit()
print("UNRESTORABLE")