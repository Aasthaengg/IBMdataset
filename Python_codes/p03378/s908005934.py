n, m, x = map(int, input().split())
a = list(map(int, input().split()))
costn, cost0 = 0, 0
for i in range(m):
    if a[i] > x:
        costn += 1
    else:
        cost0 += 1
print(min(costn, cost0))
