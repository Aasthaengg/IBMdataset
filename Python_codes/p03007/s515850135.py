n = int(input())
a = list(map(int, input().split()))

a.sort()
if a[0] * a[-1] <= 0:
    total = 0
    for i in a:
        total += abs(i)
    print(total)
    now = a[-1]
    for i in range(0, n - 2):
        if a[i + 1] > 0:
            print(min(a[i], now), max(a[i], now))
            now = -1 * abs(a[i] - now)
        else:
            print(now, a[i])
            now -= a[i]
    if a[-2] > 0:
        print(a[-2], now)
    else:
        print(now, a[-2])

elif a[0] > 0:
    total = sum(a) - 2 * a[0]
    print(total)
    now = a[0]
    for i in range(1, n - 1):
        print(now, a[i])
        now -= a[i]
    print(a[-1], now)

else:
    total = -1 * sum(a) + 2 * a[-1]
    print(total)
    now = a[n - 1]
    for i in range(n - 2, -1, -1):
        print(now, a[i])
        now -= a[i]
