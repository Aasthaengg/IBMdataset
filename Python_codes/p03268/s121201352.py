n, k = map(int, input().split())
e = 0
h = 0
for i in range(1, n + 1):
    if k % 2 == 0 and i % k == k // 2:
        h += 1
    if i % k == 0:
        e += 1
print(h * h * h + e * e * e)
