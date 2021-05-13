W, a, b = map(int, input().split())
d = b - (a + W) if a < b else a - (b + W)
print(max(d, 0))