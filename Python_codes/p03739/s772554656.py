n = int(input())
a = [int(x) for x in input().split()]

#偶数番目を正にする場合

s = 0
t0 = 0

if a[0] > 0:
    s = a[0]
else:
    s = 1
    t0 = abs(a[0]) + 1

for i in range(1, n):
    if (s + a[i]) * (-1) ** i <= 0:
        t0 += abs(s + a[i]) + 1
        s = (-1) ** i
    else:
        s += a[i]

#偶数番目を負にする場合

s = 0
t1 = 0

if a[0] < 0:
    s = a[0]
else:
    s = -1
    t1 = abs(a[0]) + 1

for i in range(1, n):
    if (s + a[i]) * (-1) ** (i + 1) <= 0:
        t1 += abs(s + a[i]) + 1
        s = (-1) ** (i + 1)
    else:
        s += a[i]

ans = min(t0, t1)

print(ans)