n, t = map(int, input().split())
a = list(map(int, input().split()))
m = [a[i] for i in range(n)]
for i in range(n - 2, -1, -1):
  m[i] = max(m[i], m[i + 1])
d = 0
ans = 0
for i in range(n):
  if d < m[i] - a[i]:
    d = m[i] - a[i]
    ans = 1
  elif d == m[i] - a[i]:
    ans += 1
print(ans)
