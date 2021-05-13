[x,y] = [int(i) for i in input().split()]
ans = 0
if x == y:
  print(1)
else:
  while x <= y:
    x *= 2
    ans += 1
  print(ans)