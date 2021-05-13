s = input()
is_there = [False for i in range(26)]


for c in s:
    is_there[ord(c)-97] = True

if len(s) == 26:
    flag = True
    buf = []
    rep = None
    for i in range(25):
        buf.append(s[-i-1])
        for b in buf:
            if ord(b) > ord(s[-i-2]):
                rep = -i-2
                flag =False
                break
        if not flag:
            break


    if flag:
        print(-1)
    else:
        tp = s[:rep]
        tails = list(s[rep:])
        tails.sort()
        # print(rep)
        for t in tails:
            if ord(t) > ord(s[rep]):
                print(tp+t)
                break
else:
    for i in range(26):
        if not is_there[i]:
            print(s+chr(i+97))
            break