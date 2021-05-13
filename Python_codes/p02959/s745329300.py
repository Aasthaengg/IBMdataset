n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
viran = 0
for i in range(n):
    if a[i] + a[i + 1] - b[i] >= 0:
        viran += b[i]
        if a[i] > b[i]:
            a[i] -= b[i]
        else:
            b[i] -= a[i]
            a[i] = 0
            a[i + 1] -= b[i]
        b[i] = 0
    else:
        viran += a[i] + a[i + 1]
        a[i] = 0
        a[i + 1] = 0
        b[i] -= a[i] + a[i + 1]
print(viran)