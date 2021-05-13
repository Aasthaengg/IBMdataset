S=input()
T=input()

A=len(S)
B=len(T)

if A<B:
    print("UNRESTORABLE")
    exit()

X=[]
for i in range(A-B+1):
    U=S[i:i+B]

    F=True
    for k in range(B):
        F&=(U[k]=="?" or U[k]==T[k])

    if F:
        Y=S[:i]+T+S[i+B:]
        Y=Y.replace("?","a")
        X.append(Y)

if X:
    print(min(X))
else:
    print("UNRESTORABLE")