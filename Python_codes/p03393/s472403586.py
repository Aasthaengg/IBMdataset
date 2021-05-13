s = input(); a = []; b = [0]*27; t = ""
for i in range(len(s)): a.append(ord(s[i])); b[a[i]-97] = 1
if s == "zyxwvutsrqponmlkjihgfedcba": print(-1)
else:
    for i in range(27):
        if b[i] == 0: c = i; break
    if c != 26:
        a.append(c+97)
        for i in range(len(a)): t += chr(a[i])
        print(t)
    else:
        d = []
        for _ in range(24):
            if a[-2] > a[-1]: d.append(a.pop())
            else:
                d.append(a.pop()); d.sort()
                break
        else: d.append(a.pop()); d.sort()
        for i in range(len(d)):
            if a[-1] < d[i]: a.pop(); a.append(d[i]); break
        for i in range(len(a)): t += chr(a[i])
        print(t)