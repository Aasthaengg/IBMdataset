S = input()
T = input()

S_d = dict()
T_d = dict()
for i in range(len(S)):
    S_d.setdefault(S[i], T[i])
    if S_d[S[i]] != T[i]:
        print('No')
        exit(0)
    T_d.setdefault(T[i], S[i])
    if T_d[T[i]] != S[i]:
        print('No')
        exit(0)
print('Yes')
