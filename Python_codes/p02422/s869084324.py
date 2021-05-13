S,Q,*C = open(0).read().split()
s = list(S)

i = 0
while i < len(C):
    cmd = C[i]
    i += 1
    if cmd == "replace":
        a = int(C[i])
        b = int(C[i+1])
        p = C[i+2]
        i += 3
        for j in range(a, b+1):
            s[j] = p[j - a]
    elif cmd == "reverse":
        a = int(C[i])
        b = int(C[i+1])
        i += 2
        r = list(reversed(s[a:b+1]))
        for j, c in enumerate(r):
            s[j + a] = c
    elif cmd == "print":
        a = int(C[i])
        b = int(C[i+1])
        i += 2
        print("".join(s[a:b+1]))
    else:
        print(cmd)
        break

