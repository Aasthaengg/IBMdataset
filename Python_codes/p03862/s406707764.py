from copy import deepcopy
N, x = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(N - 1):
    if a[i] + a[i + 1] > x:
        c += a[i] + a[i + 1] - x
        a[i + 1] -= a[i] + a[i + 1] - x
        if a[i + 1] < 0:
            a[i] -= -a[i + 1]
            a[i + 1] = 0
print(c)