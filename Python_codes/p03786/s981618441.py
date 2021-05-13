from copy import copy
n, *a = map(int, open(0).read().split())
a.sort()
b = copy(a)
for i in range(n - 1):
    b[i + 1] += b[i]

ans = 0
for i in range(n - 1):
    if b[i] * 2 < a[i + 1]:
        ans = i + 1
print(n - ans)
