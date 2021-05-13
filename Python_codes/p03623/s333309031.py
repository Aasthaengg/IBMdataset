x, a, b = list(map(int, input().split()))
print(['A', 'B'][int(abs(a - x) > abs(b - x))])
