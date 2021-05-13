x, y = map(int, input().split())
print(x if not x % y == 0 else -1)