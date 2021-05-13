n, m = map(int, input().split())

if n == 1 and m == 1:
    print(1)
elif n <= 2 and m <= 2:
    print(0)
elif (n >= 3 and m == 1) or (n == 1 and m >= 3):
    print(max(n, m) - 2)
elif (n >= 3 and m == 2) or (n == 2 and m >= 3):
    print(0)
elif n >= 3 and m >= 3:
    print((n - 2) * (m - 2))