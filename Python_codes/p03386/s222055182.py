a, b, k = map(int, input().split())
L =[]
for i in range(k):
    L.append(a + i)
    if a + i == b:
        break
for j in range(k):
    L.append(b - j)
    if b - j == a:
        break
L = list(set(L))
for k in sorted(L):
    print(k)
