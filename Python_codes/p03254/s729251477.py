n, y = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0
if y == sum(a):
  ans = n
elif y > sum(a):
  ans = n -1
else:
  for i in range(n):
    if y - a[i] >= 0:
      y -= a[i]
      ans += 1
    else:
      break
print(ans)