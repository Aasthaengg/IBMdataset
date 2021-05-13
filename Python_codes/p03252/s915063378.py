S=input()
T=input()

sd={}
td={}
cond=True
for i in range(len(S)):
    if S[i] not in sd:
        sd[S[i]]=T[i]
    else:
        if sd[S[i]]!=T[i]:
            cond=False
            break
    if T[i] not in td:
        td[T[i]]=S[i]
    else:
        if td[T[i]]!=S[i]:
            cond=False
            break

if cond:
    print("Yes")
else:
    print("No")