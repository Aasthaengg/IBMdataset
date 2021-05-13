n, a, b = map(int, input().split())
H = [int(input()) for _ in range(n)]

l = 0
r = 10 ** 18

while r - l > 1:
  m = (r + l) // 2
  li = [h - b * m for h in H]
  cnt = sum([(i - 1) // (a - b) + 1 if i > 0 else 0 for i in li])
  if cnt <= m:
    r = m
  else:
    l = m
print(r)