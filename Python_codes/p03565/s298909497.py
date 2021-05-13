S = input().strip()
N = len(S)
T = input().strip()
K = len(T)
flag = 0
ind = -1
for i in range(N-K,-1,-1):
    A = list(S[i:i+K])
    flag = 0
    for j in range(K):
        if A[j]!="?" and A[j]!=T[j]:
            flag = 1
            break
    if flag == 0:
        ind = i
        break
if ind<0:
    print("UNRESTORABLE")
else:
    S = list(S)
    for j in range(K):
        if S[ind+j]=="?":
            S[ind+j] = T[j]
    for i in range(N):
        if S[i]=="?":
            S[i]="a"
    print("".join(S))