n, k = map(int, input().split())

s = []
for a in range(1, n + 1):
    if (2 * a) % k == 0:
        s.append(a)

t = []
for a in range(1, n + 1):
    if a % k == 0:
        t.append(a)

print((len(s) - len(t)) ** 3 + len(t) ** 3)