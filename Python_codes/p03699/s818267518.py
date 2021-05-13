n = int(input())
s = []
for i in range(n):
  s.append(int(input()))
ans = sum(s)
if ans % 10 == 0:
  s.sort()
  f = 0
  for i in range(n):
    if s[i] % 10 == 0:
      next
    else:
      ans -= s[i]
      f = 1
      break
  if f == 0:
    ans = 0
print(ans)