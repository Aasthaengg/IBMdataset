import copy
S = list(input())
T = list(input())
N = len(S)
M = len(T)
lst = []

for i in range(N-M+1):
    for j in range(M):
        if (T[j] == S[i+j]) or (S[i+j] == "?"):
            exist = True
        else:
            exist = False
            break
    if exist:
        ref = copy.copy(S)
        for k in range(M):
            ref[i+k] = T[k]
        s = "".join(ref)
        s = s.replace("?","a")
        lst.append(s)

lst = sorted(lst)

if lst == []:
    print("UNRESTORABLE")
else:
    print(lst[0])
