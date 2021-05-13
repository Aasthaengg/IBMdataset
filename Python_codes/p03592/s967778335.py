n, m, k = map(int, input().split())
L = set()
for i in range(m + 1):
    for j in range(n + 1):
        c = n * i + m * j - i * j * 2
        if c >= 0:
            L.add(c)
if k in L:
    print('Yes')
else:
    print('No')
