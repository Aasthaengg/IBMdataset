def dist(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])


h, w, d = map(int, input().split())

table = {}

for i in range(h):
    a = list(map(int, input().split()))
    for j in range(w):
        table[a[j]] = (j + 1, i + 1)

cum = [0] * (h * w + 1)
for i in range(h * w + 1):
    if i > d:
        cum[i] = cum[i - d] + dist(table[i], table[i - d])


q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(cum[r] - cum[l])

