a, b, c = [int(item) for item in input().split()]
print(min(b, c), max((b+c) - a, 0))