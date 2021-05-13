a, b, c = map(int, input().split())

print(0 if any(map(lambda x: x % 2 == 0, [a, b, c])) else min(
    a * b, b * c, c * a))