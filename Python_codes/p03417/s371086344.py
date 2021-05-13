n, m = map(int, input().split())
if n > m:
  n, m = m, n
if n == 1:
  if m == 1:
    ans = 1
  else:
    ans = m - 2
else:
  ans = (n - 2) * (m - 2)
print(ans)