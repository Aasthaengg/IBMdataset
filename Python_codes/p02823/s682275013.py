n, a, b = map(int, input().split())

if (a - b) % 2 == 0:
    print(abs(a - b) // 2)
else:
    a, b = min(a, b), max(a, b)
    t = a + (b - a - 1) // 2
    k = (n - b + 1) + (- a + b - 1) // 2
    print(min(t, k))