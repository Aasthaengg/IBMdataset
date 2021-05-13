n, m = map(int, input().split())

min_l = 0
max_l = 10**6

for _ in range(m):
    L, R = map(int, input().split())
    min_l = max(min_l, L)
    max_l = min(max_l, R)

print(max_l - min_l + 1 if max_l - min_l + 1 > 0 else 0)