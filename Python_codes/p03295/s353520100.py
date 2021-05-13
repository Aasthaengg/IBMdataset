n, m = map(int, input().split())
L = list()
for i in range(m):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    L.append([x, y])
L = sorted(L, key=lambda x: x[1])
A = L[0]
i = 1
for v in L:
    if v[0] >= A[1]:
        A = v
        i += 1
print(i)