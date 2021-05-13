n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = [0] * (n + 1)
sb = [0] * (m + 1)
for i in range(n):
  sa[i + 1] = sa[i] + a[i]
for i in range(m):
  sb[i + 1] = sb[i] + b[i]
r = m
ans = 0
for i in range(n + 1):
  if sa[i] > k:
    break
  while sa[i] + sb[r] > k:
    r -= 1
  ans = max(ans, i + r)
print(ans)