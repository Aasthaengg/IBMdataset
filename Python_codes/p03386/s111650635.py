a, b, k = list(map(int, input().split()))
if b - a + 1 > 2 * k:
    [print(i) for i in range(a, a + k)]
    [print(i) for i in range(b - k + 1, b + 1)]
else:
    [print(i) for i in range(a, b + 1)]