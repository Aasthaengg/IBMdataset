n,m = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0
for i in ab:
  t = min(m,i[1])
  ans += i[0]*t
  m -= t
print(ans)