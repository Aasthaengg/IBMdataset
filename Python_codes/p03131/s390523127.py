k, a, b = map(int, input().split())

if b - 2 <= a or k < a + 1:
    print(k + 1)
else:
    r = k - (a - 1)
    print((r // 2 - 1) * (b - a) + b + r % 2)