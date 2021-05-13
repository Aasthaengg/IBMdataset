import bisect

while 1:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    L = list(range(1, n + 1))
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            a = x - L[i] - L[j]
            idx = bisect.bisect_left(L, a, lo=j + 1)
            if idx < n and L[idx] == a:
                count += 1
    print(count)