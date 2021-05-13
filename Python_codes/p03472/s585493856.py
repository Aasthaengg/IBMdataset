def get_ints():
  return list(map(int, input().split()))

n, h = get_ints()
maxHit = 0
throw = []
for i in range(n):
  x, y = get_ints()
  maxHit = max(maxHit, x)
  throw.append(y)

throw.sort()
throw.reverse()
ans = 0
for d in throw:
  if h <= 0:
    print(ans)
    exit(0)
  if d <= maxHit:
    break
  h -= d
  ans += 1

print(ans + (h + maxHit - 1) // maxHit)

