N = int(input())
a = [int(input()) for _ in range(N)]
a.sort()

if N % 2 == 0:
    res = 2 * (sum(a[N // 2:]) - sum(a[:N // 2]))
    res += a[N // 2 - 1] - a[N // 2]
    print(res)
else:
    res = 2 * (sum(a[N // 2 + 1:]) - sum(a[:N // 2]))
    print(res - min(a[N // 2 + 1] - a[N // 2], a[N // 2] - a[N // 2 - 1]))
