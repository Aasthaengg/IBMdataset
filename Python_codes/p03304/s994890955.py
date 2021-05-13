n, m, d = map(int, input().split())


count = 0
if d == 0:
    print (n * (m - 1) / (n ** 2))
elif n % 2 == 0:
    N = n // 2
    count += min(d, N)
    count += 2 * max(0, (N - d))
    count *= 2
    print (count * (m - 1) / (n ** 2))
else:
    N = n // 2
    count += min(d, N)
    count += 2 * max(0, (N - d))
    count *= 2
    if N + 1 > d:
        count += 2
    # print (count)
    print (count * (m - 1) / (n ** 2))
