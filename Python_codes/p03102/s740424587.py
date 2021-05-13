n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for i in range(n):
  a = list(map(int, input().split()))
  delta = 0
  for j in range(m):
    delta += a[j]*b[j]
  delta += c
  if delta > 0:
    ans += 1
  else:
    continue
print(ans)