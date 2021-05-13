n, y = map(int, input().split())

s = '-1 -1 -1'
for i in range(n + 1):
    for j in range(n + 1 - i):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            s = '{} {} {}'.format(i, j, n - i - j)
print(s)
