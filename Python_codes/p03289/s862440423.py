S = input()

if S[0] == "A":
    T = S[2:-1]
    flag = 0
    ok = -1
    for i in T:
        if i == "C" and flag ==0:
            ok = T.index("C")
            flag = 1
        elif i == "C" and flag == 1:
            ok = -1
            break
    if ok >= 0:
        H = S[1:]
        F = H[:ok+1] + H[ok+2:]
        t = False
        for k in F:
            if k.isupper():
                t = True
        if not t:
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")