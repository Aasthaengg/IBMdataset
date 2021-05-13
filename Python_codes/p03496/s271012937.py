


n = int(input())
a = list(map(int, input().split()))


res = []
mx = max(a)
mx_idx = a.index(mx)
mn = min(a)
mn_idx = a.index(mn)

if abs(mx) >= abs(mn):
    for i in range(n):
        res.append((mx_idx, i))
    for i in range(0, n - 1):
        res.append((i, i + 1))
else:
    for i in range(n):
        res.append((mn_idx, i))
    for i in range(n - 1, 0, -1):
        res.append((i, i - 1))

print(len(res))

for i, j in res:
    print("%d %d" % (i + 1, j + 1))

