n, m, d = map(int, input().split(' '))
if d >= n:
    print(0)
else:
    unit = (n - d) / (n ** 2)
    if d != 0:
        unit *= 2
    ans = unit * (m - 1)
    print(ans)