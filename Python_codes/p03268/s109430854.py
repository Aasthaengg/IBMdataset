n, k = map(int, input().split())
if k % 2 == 0:
    t = (n + k // 2) // k
    print(t ** 3 + (n // k) ** 3)
else:
    t = n // k
    print(t ** 3)
