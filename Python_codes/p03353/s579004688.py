S=input()
K=int(input())
L=[""]
for s in range(len(S)):
    for e in range(s,len(S)):
        #print(S[s:e+1])
        if S[s:e+1] in L:
            continue
        if len(L)>K:
            if S[s:e+1]>L[K]:
                break
        if S[s:e+1] not in L:
            if len(L)<=K:
                L.append(S[s:e+1])
                L.sort()
            else:
                L.append(S[s:e+1])
                L.sort()
                L=L[:K+1]
                #print(L)
print(L[-1])