N, M = map(int, input().split())
items = [ tuple(map(int, input().split())) for _ in range(N) ]
items.sort()
ans = 0
m = 0
for item in items:
  a = min(M - m, item[1])
  m += a
  ans += a * item[0]
print(ans)