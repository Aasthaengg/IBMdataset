n, m = map(int, input().split())
l = []
for i in range(n):
  a, b = map(int, input().split())
  l.append([a, b])
s = sorted(l, key=lambda x:x[0])
ans = 0
for i in range(n):
  a, b = s[i]
  if b <= m:
    ans += a*b
    m -= b
  else:
    ans += a*m
    break
print(ans)