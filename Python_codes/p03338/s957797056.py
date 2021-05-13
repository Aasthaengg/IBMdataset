n = int(input())
s = list(input())

ans = 0
for i in range(1,n-1):
  t = len(set(s[:i]) & set(s[i:]))
  if ans < t: ans = t
print(ans)