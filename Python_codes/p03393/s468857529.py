s = input()
alp = "abcdefghijklmnopqrstuvwxyz"
if len(s) == 26:
    bck = []
    for i in range(25):
        bck.append(s[25-i])
        if s[25-i] > s[24-i]:
            for j in range(alp.find(s[24-i]),26):
                if alp[j] in bck:
                    sn = alp[j]
                    break
            print(s[0:24-i]+sn)
            exit()
    print(-1)
else:
    for i in alp:
        if i in s:
            continue
        else:
            print(s+i)
            exit()
