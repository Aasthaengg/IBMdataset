n, m = map(int, input().split())
max_l = 0
min_r = 10**5
for i in range(m):
  l, r = map(int, input().split())
  if l > max_l:
    max_l = l
  if r < min_r:
    min_r = r
res = min_r - max_l + 1
if res<0:
  res = 0
print(res)
