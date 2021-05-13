sa = input()
s = list(sa)
a = [chr(ord('a') + i) for i in range(26)]
if sa == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif len(s) != 26:
    for i in range(len(a)):
        if a[i] not in s:
            s.append(a[i])
            print("".join(s))
            exit()
else:
    used = [s[25]]
    for i in range(25, 0, -1):
        if a.index(s[i-1]) > a.index(s[i]):
            used.append(s[i-1])
        else:
            for j in range(a.index(s[i-1])+1, 26):
                if a[j] in used:
                    s[i-1] = a[j]
                    print("".join(s[:i]))
                    exit()




