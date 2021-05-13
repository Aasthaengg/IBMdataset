n, a, b = map(int, input().split())
max_ = min(a, b)
min_ = max(a + b - n, 0)
print(max_, min_)