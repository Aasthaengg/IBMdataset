s = input()
n = len(s)
ans = 0

for c in s:
  ans += int(c)

for i in range(n):
  res =0 
  d = int(s[i])
  if d==0:
    continue
  else:
    d -= 1
  for c in s[:i]:
    res += int(c)
  res += d
  res += (n-i-1)*9
  ans = max(ans, res)
print(ans)

