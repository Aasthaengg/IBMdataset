
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

res = []
for a in A:
    for b in B:
        res.append(a + b)

res.sort(reverse=True)

res2 = []
for v in res[:K]:
    for c in C:
        res2.append(v + c)

res2.sort(reverse=True)
for i in range(K):
    print(res2[i])
