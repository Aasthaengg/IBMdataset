n, a, b = map(int, input().split())
min_num = max(0, a + b - n)
max_num = min(a, b)
print(*[max_num, min_num])