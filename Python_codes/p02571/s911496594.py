s = input()
t = input()

n = len(s)
m = len(t)
ans = 10**9

for i in range(n-m+1):
  res = 0
  u = s[i:i+m]
  for j in range(m):
    if t[j]!=u[j]:
      res += 1
  ans = min(ans, res)

print(ans)
