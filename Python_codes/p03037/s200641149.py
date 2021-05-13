n, m = map(int, input().split())
max_l = 0
min_r = 10 ** 10
for _ in range(m):
  l, r = map(int, input().split())
  max_l = max(max_l, l)
  min_r = min(min_r, r)
print(max(0, min_r - max_l + 1))