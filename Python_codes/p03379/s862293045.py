n = int(input())
X = list(map(int, input().split()))

import copy
Y = copy.copy(X)

L = []
U = []
X.sort()
for i in range(n):
    if i < n//2:
        L.append(X[i])
    else:
        U.append(X[i])
#print(L)
#print(U)

L_ = set(L)
U_ = set(U)

ans = [0]*n
for i, y in enumerate(Y):
    if y in L_:
        ans[i] = U[0]
    else:
        ans[i] = L[-1]
print(*ans, sep='\n')
