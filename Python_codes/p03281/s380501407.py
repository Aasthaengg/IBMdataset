import math
def prime(x):
  p = {}
  last = math.floor(x ** 0.5)
  if x % 2 == 0:
    cnt = 1
    x //= 2
    while x & 1 == 0:
      x //= 2
      cnt += 1
    p[2] = cnt
  for i in range(3, last + 1, 2):
    if x % i == 0:
      x //= i
      cnt = 1
      while x % i == 0:
        cnt += 1
        x //= i
      p[i] = cnt
  if x != 1:
    p[x] = 1
  return p


N = int(input())

ans = 0
for i in range(1, N + 1, 2):
  p = prime(i)
  t = 1
  for v in p.values():
    t *= v + 1
  if t == 8:
    ans += 1

print(ans)