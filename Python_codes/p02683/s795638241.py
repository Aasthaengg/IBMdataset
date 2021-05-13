N,M,X = map(int,input().split())
C = []
A = []
for i in range(N):
    L = list(map(int,input().split()))
    C.append(L[0])
    A.append(L[1:M+1])
import itertools
L = []
Num = [i for i in range(N)]
for i in range(1,N+1):
    for j in itertools.combinations(Num,i):
        L.append(list(j))
c = 20000000
for i in range(len(L)):
    Z = [0 for _ in range(M)]
    m = 0
    for j in range(len(L[i])):
        for k in range(M):
            Z[k] += A[L[i][j]][k]
        m += C[L[i][j]]
    for l in range(M):
        if Z[l] < X:
            break
        if l == M-1:
            c = min(c,m)
if c == 20000000:
    print(-1)
else:
    print(c)