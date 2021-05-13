n, a, b = map(int, input().split())
max_sub = min(a, b)
min_sub = max_sub - (n-max(a, b))

print(max_sub, min_sub if min_sub > 0 else 0)