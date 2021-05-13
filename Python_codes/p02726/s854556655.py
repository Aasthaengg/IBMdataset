n, x, y = map(int, input().split())
l = [0]*(n - 1)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        a = abs(j - i)
        b = abs(x - i) + abs(y - j) + 1
        d = min(a, b)
        l[d - 1] += 1

for i in l:
    print(i)