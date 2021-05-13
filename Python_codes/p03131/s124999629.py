k, a, b = map(int, input().split())
if b - a <= 2:
    print(k + 1)
else:
    cnt = max(0, k - (a - 1))
    print((b - a) * (cnt // 2) + 1 * cnt % 2 + min(k, a))