S = input().strip()
N=len(S)
T = input().strip()
M=len(T)
A = []
for i in range(N-M+1):
    flag = 0
    for j in range(i,i+M):
        if S[j]=="?" or S[j]==T[j-i]:continue
        else:
            flag=1
            break
    if flag==0:
        X = list(S)
        for j in range(i,i+M):
            X[j] = T[j-i]
        for i in range(N):
            if X[i]=="?":
                X[i]="a"
        A.append(X)
if len(A)==0:
    print("UNRESTORABLE")
else:
    A = sorted(A)
    print("".join(A[0]))