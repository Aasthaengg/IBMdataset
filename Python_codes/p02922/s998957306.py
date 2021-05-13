a = list(map(int,input().split()))
c = 1
ans = 0
if a[1] == 1:
  print(0)
else:
  while a[1] > c:
    c += (a[0]-1)
    ans += 1
  print(ans)
