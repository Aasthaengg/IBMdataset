n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))

u = []
l = []

for i in range(m):
    if a[i] < x:
        l.append(a[i])
    elif a[i] > x:
        u.append(a[i])

print(min(len(u), len(l)))