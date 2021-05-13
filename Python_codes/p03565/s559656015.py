s = input()
t = input()
ans = "UNRESTORABLE"
for begin in range(len(s)):#塗り替えるとこの始点
    if begin+len(t) > len(s):
        break
    tmp = list(s)
    ti = 0
    for i in range(begin,begin+len(t)):
        tmp[i] = t[ti]
        ti += 1
    for i in range(len(s)):
        if s[i] != '?':
            if s[i] != tmp[i]:
                break
    else:
        for i in range(len(s)):
            if tmp[i] == "?":
                tmp[i] = 'a'
        ans = "".join(tmp)
print(ans)