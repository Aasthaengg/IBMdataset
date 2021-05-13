from string import ascii_lowercase
s = input()

if s == ascii_lowercase[::-1]:
    print(-1)
elif len(s)!=len(ascii_lowercase):
    s1 = set(list(s))
    s2 = set(list(ascii_lowercase))
    w = min(s2-s1)
    print(s+w)
else:
    back = ''
    tmp = ''
    pos = 0
    for i in range(len(s))[::-1]:
        if i==25:
            back += s[i]
            tmp = s[i]
        elif s[i]>tmp:
            back += s[i]
            tmp = s[i]
        else:
            pos = i
            break
    
    res = s[:pos]
    w = s[pos]
    l = []
    for b in back:
        if b > w:
            l.append(b)
    print(res + min(l))
