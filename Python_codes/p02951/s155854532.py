a, b, c = map(int, input().split())
r = a - b
print(0 if c <= r else c - r)
