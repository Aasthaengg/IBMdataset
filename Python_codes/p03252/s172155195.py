

S = input()
T = input()


dS = {}
dT = {}
for i in range(len(S)):
    dS.setdefault(T[i], S[i])
    if dS[T[i]] != S[i]:
        print("No")
        exit()
    dT.setdefault(S[i], T[i])
    if dT[S[i]] != T[i]:
        print("No")
        exit()
        


print("Yes")