X = open(0).readlines()
S = X[0].strip()
T = X[1].strip()
m, n = len(T), len(S)
if m > n:
    print('UNRESTORABLE')
else:
    for i in range(n-m, -1, -1):
        U = S[i:i+m]
        if all(u == t or u == '?' for u, t in zip(U, T)):
            V = list(S.replace('?', 'a'))
            for j in range(m):
                V[i+j] = T[j]
            print(''.join(V))
            break
    else:
        print('UNRESTORABLE')