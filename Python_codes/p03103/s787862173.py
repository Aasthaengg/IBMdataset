n, m = map(int, input().split())
l = []
for i in range(n):
  a, b = map(int, input().split())
  l.append([a, b])

l.sort()
ans = 0
for i in range(n):
  if l[i][1] <= m:
    ans += l[i][0] * l[i][1]
    m -= l[i][1]
  else:
    ans += l[i][0] * m
    break
print(ans)