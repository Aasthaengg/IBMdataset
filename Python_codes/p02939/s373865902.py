s = input()
L = []
i = 0
pre = ''
while i < len(s):
    c = s[i]
    if c == pre:
        if i == len(s) - 1:
            break
        c += s[i+1]
        i += 1
    L.append(c)
    pre = c
    i += 1
print(len(L))
