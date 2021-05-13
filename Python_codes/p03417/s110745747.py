n, m = list(map(int, input().split()))
if n == m == 1:
    print(1)
elif n == 1 or m == 1:
    print(n * m - 2)
else:
    print(n * m - 2 * (n + m - 2))
