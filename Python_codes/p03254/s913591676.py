n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
if sum(a) == x:
  ans = n
elif x < min(a):
  ans = 0
else:
  if sum(a) < x:
    ans = n - 1
  else:
    a.sort()
    k = 0
    for e in a:
      k += e
      if k <= x:
        ans += 1
      else:
        break
print(ans)