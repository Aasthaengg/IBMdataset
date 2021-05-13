x, k, d = map(int, input().split())

if x + k * d <= 0:
    print(-(x + k * d))
elif x - k * d >= 0:
    print(x - k * d)
elif x >= 0:
    print(min([abs(x - (k - 2 * i) * d) for i in range((k * d - x) // (2 * d) - 100, (k * d - x) // (2 * d) + 100)]))
else:
    print(min([abs(x + (k - 2 * i) * d) for i in range((k * d + x) // (2 * d) - 100, (k * d + x) // (2 * d) + 100)]))
