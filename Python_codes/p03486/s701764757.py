s=input()
t=input()

if s==t:
    print("No")
else:
    flg=(len(s)<len(t))
    for a in s:
        if not(a in t):
            flg=False
            break
    if flg:
        print("Yes")
    else:
        flg=False
        for a in s:
            for b in t:
                if ord(a)<ord(b):
                    flg=True
                    break
            if flg:
                break
        if flg:
            print("Yes")
        else:
            print("No")