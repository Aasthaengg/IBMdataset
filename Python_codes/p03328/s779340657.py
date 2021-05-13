a, b = map(int, input().split())
d = b - a
r = (d * (d + 1)) // 2
print(r - b)