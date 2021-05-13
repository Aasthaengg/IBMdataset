x, y = map(int, input().split())

ans = 0
Button = [(1, 1), (1, 0), (0, 1), (0, 0)]

ans = float("INF")
for fb, lb in Button:
  t, tx, ty = 0, x, y
  if fb:
    tx = -x
    t += 1
  if lb:
    ty = -y
    t += 1
  if tx > ty:
    continue
  t += ty - tx
  ans = min(ans, t)

print(ans)