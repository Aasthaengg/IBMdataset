a, b = list(map(int, input().split()))
if abs(a - b) >= 1:
    print(2 * max(a, b) - 1)
else:
    print(a + b)