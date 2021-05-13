n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a, count = [], 0
for _ in range(n):
    a.append(list(map(int, input().split())))
for k in range(n):
    s = 0
    for i, j in zip(a[k], b):
        s += i*j
    if s+c > 0:
        count += 1
print(count)