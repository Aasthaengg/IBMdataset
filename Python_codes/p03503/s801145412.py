import itertools
n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]
ans = -(10**10)
for l in itertools.product(range(2), repeat=10):
  if sum(l) == 0:
    continue
  s = 0
  for i in range(n):
    c = 0
    for j in range(10):
      c += l[j] * f[i][j]
    s += p[i][c]
  ans = max(ans, s)
print(ans)
