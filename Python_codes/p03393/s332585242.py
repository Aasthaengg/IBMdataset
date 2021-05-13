S=input()
R="zyxwvutsrqponmlkjihgfedcba"
A=set(R)
if len(S)<=25:
    print(S+min(A-set(S)))
elif S==R:
    print(-1)
else:
    ok=set()
    while S:
        ok.add(S[-1])
        S=S[:-1]
        L=[s for s in ok if s > S[-1]]
        if L:
            print(S[:-1]+min(L))
            break
