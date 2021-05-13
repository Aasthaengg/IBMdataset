import sys
N, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
a.sort()
if a[0]>x:
  print(0)
  sys.exit()
for i in range(N):
  x -= a[i]
  if x < 0:
    print(ans)
    sys.exit()
  ans += 1
if x > 0:
  print(ans-1)
else:
  print(ans)