(n, m, d) = map(int, input().split())
if d == 0:
    print((m-1) / float(n))
else:
    print(2 * (m-1) * (n-d) / float(n * n))
