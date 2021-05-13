S=input()
T=input()
N=len(S)
d=dict()
for i in range(N):
    if S[i] not in d.keys():
        if T[i] in d.values():
            print("No")
            break
        d[S[i]]=T[i]
    else:
        if d[S[i]]!=T[i]:
            print("No")
            break
else:
    print("Yes")
