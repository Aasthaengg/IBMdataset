n, a, b = map(int, input().split())

max_ = min(a, b)

if max(n, a+b) == a+b:
    min_ = a + b - n
else:
    min_ = 0

print(max_, min_)