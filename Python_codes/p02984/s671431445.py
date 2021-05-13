n = int(input())
a = list(map(int, input().split()))

d = [0] * n

for i in range(n):
    if i % 2 == 0:
        d[0] += a[i]
    else:
        d[0] -= a[i]

for i in range(1, n):
    d[i] = 2 * a[i - 1] - d[i - 1]

print(*d)
