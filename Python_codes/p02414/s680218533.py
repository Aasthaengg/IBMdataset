import math
n,m,l = map(int, input().split())
A = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
B = []
for j in range(m):
    b = list(map(int, input().split()))
    B.append(b)

C = []
for i in range(n):
    for k in range(l):
        for j in range(m):
            c = A[i][j]*B[j][k]
            C.append(c)
S = []
d = math.ceil(len(C)/(n*l))
r = [C[x: x+d] for x in range(0,len(C),d)]

for i in range(len(r)):
    s = sum(r[i])
    S.append(s)
    e = math.ceil(len(S)/n)
u = [S[y: y+e] for y in range(0,len(S),e)]
for i in range(len(u)):
    print(*u[i])
