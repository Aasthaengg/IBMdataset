n, m = map(int, input().split())
max_l = 0
min_r = n
ans = n
for i in range(m):
  l, r = map(int, input().split())
  if ans != 0:
    if l <= min_r or r <= max_l:
      max_l = max(max_l, l)
      min_r = min(min_r, r)
    else:
      ans = 0
if ans != 0:
  ans = min_r - max_l + 1
print(ans)