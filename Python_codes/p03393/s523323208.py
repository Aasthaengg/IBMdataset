s = list(input())

ss = set(s)

if len(s) < 26:
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in ss:
            print("".join(s) + c)
            exit()
else:
    suc = s[-1]
    while suc in ss and s:
        suco = ord(suc) + 1
        if suco > ord("z"):
            ss.remove(s.pop())
            if not ss:
                break
            suc = s[-1]
        else:
            suc = chr(suco)
    
    if not ss:
        print(-1)
    else:
        s[-1] = suc
        print("".join(s))
