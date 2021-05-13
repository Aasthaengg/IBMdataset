n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

table = {}

for i in range(n - 1):
    for j in range(i + 1, n):
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        if (dx, dy) not in table:
            table[(dx, dy)] = 1
            table[(-dx, -dy)] = 1
        else:
            table[(dx, dy)] += 1
            table[(-dx, -dy)] += 1

m = 0

for key, value in table.items():
    m = max(m, value)

print(n - m)
