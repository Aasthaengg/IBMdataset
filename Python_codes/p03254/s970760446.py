n, x = map(int, input().split())
a = [int(s) for s in input().split()]
count = 0

a.sort()
for i in range(n):
    if x >= a[i] and i < n - 1:
        x -= a[i]
        count += 1
    elif x == a[i] and i == n - 1:
        count += 1
print(count)