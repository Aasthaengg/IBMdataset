S = input().strip()
T = input().strip()
N = len(S)
C = {}
D = {}
flag = 0
for i in range(N):
    if S[i] not in C:
        C[S[i]] = T[i]
    elif C[S[i]]!=T[i]:
        flag = 1
        break
    if T[i] not in D:
        D[T[i]] = S[i]
    elif D[T[i]] != S[i]:
        flag = 1
        break
if flag==0:
    print("Yes")
else:
    print("No")