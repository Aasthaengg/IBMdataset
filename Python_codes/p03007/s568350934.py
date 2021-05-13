n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[0] >= 0:
    print(sum(a) - 2 * a[0])
    x, y = a[0], 0
    for i in range(n - 2):
        x -= y
        y = a[i + 1]
        print(x, y)
    x -= y
    print(a[-1], x)
elif a[-1] <= 0:
    print(-sum(a) + 2 * a[-1])
    x, y = a[-1], 0
    for i in range(n - 1):
        x -= y
        y = a[-(i + 2)]
        print(x, y)
else:
    m = 0
    c = 0
    for i in range(n):
        m += abs(a[i])
        if a[i] <= 0:
            c = i
    print(m)
    x, y = a[0], 0
    for i in range(n - 1, c + 1, -1):
        x -= y
        y = a[i]
        print(x, y)
    x -= y
    print(a[c + 1], x)
    x = a[c + 1] - x
    for i in range(1, c + 1):
        y = a[i]
        print(x, y)
        x -= y