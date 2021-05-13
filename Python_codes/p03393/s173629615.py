S=list(input())
L=[ord(s) for s in S]+[96]
for i in range(len(L)):
    l=L[-1]
    for j in range(l+1,123):
        if j not in L:
            S=S+[chr(j)]
            print(*S,sep="")
            exit()
    else:
        L.pop(-1)
        if S:
            S.pop(-1)
else:
    print(-1)