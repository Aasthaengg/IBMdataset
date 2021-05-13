a, b = map(int, input().split())
print(-1 if any(True if x > 9 else False for x in (a, b)) else a * b)