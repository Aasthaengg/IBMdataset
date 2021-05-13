s = input()
a = []
t = ""
for i in range(len(s)):
    if i == 0:
        a.append(s[i])
    else:
        t += s[i]
        if t != a[-1]:
            a.append(t)
            t = ""
        else:
            if i == len(s) - 1:
                a[-1] += t
print(len(a))
