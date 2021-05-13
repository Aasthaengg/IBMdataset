d,n = map(int,input().split())
ans = 0
if d == 0:
  ans = n
elif d == 1:
  ans = 100 * n
else:
  ans = 10000 * n
if n == 100:
  if d == 0:
    ans += 1
  elif d == 1:
    ans += 100
  else:
    ans += 10000
print(ans)