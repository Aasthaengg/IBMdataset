n = int(input())
s = list(input())
ans = 0
for i in range(1,n-1):
  a = set(s[:i])
  b = s[i:]
  t = 0
  for j in a:
    if j in b:
      t += 1
  ans = max(ans, t)
print(ans)