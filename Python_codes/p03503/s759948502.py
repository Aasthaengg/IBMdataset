X = open(0).readlines()
n = int(X[0])
F = []
for x in X[1:n+1]:
    F.append(list(map(int, x.split())))
P = []
for x in X[n+1:]:
    P.append(list(map(int, x.split())))

ans = -10**10
for i in range(1, 2**10):
    A = [(i >> j) & 1 for j in range(10)]
    s = 0
    for j in range(n):
        c = sum(p and a for p, a in zip(F[j], A))
        s += P[j][c]
    if ans < s:
        ans = s
print(ans)