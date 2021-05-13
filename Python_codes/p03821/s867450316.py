n = int(input())
l = []
r = []
for _ in range(n):
  a, b = map(int, input().split())
  l.append(a)
  r.append(b)
before_sa = 0
for i in range(1, n+1):
  a, b = l[-i], r[-i]
  a += before_sa
  if a % b == 0:
    continue
  else:
    sa = (a//b + 1) * b - a
    before_sa += sa
print(before_sa)
