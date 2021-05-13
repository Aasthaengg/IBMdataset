n, k = map(int, input().split())

x = 0
for a in range(1, n + 1):
    if (2 * a) % k == 0:
        x += 1

y = 0
for a in range(1, n + 1):
    if a % k == 0:
        y += 1

print((x - y) ** 3 + y ** 3)
