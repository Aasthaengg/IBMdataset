X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = []
for a in A:
    for b in B:
        D.append(a + b)
D.sort(reverse=True)
if len(D) > K:
    D = D[:K]
E = []
for d in D:
    for c in C:
        E.append(c + d)

E.sort(reverse=True)
for i, e in enumerate(E):
    if i >= K:
        break
    print(e)