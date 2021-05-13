ans = 0
n, a, b = map(int, input().split())
for i in range(1, n + 1):
  t = 0
  z = i
  while z > 0:
    t = t + z % 10
    z = z // 10
  if t >= a and t <= b:
    ans = ans + i
print(ans)