sd = input()
t = input()
oks = []
if len(sd) < len(t):
    print("UNRESTORABLE")
else:
    for i in range(len(sd)-len(t)+1):
        sdd = sd[i:i+len(t)]
        f = True
        for j,sddj in enumerate(sdd):
            if sddj == "?":
                continue
            elif sddj != t[j]:
                f = False
                break
        if f:
            oks.append(i)
    if oks:
        k = oks[-1]
        print((sd[:k]+t+sd[k+len(t):]).replace("?","a"))
    else:
        print("UNRESTORABLE")