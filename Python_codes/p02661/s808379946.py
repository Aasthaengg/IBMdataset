n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

a = [x[0] for x in ab]
a.sort()
b = [y[1] for y in ab]
b.sort()

if n % 2 == 0:
    print((b[n // 2 - 1] + b[n // 2]) - (a[n // 2 - 1] + a[n // 2]) + 1)
else:
    print(b[(n - 1) // 2] - a[(n - 1) // 2] + 1)