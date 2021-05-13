n = int(input())
li = [int(input()) for i in range(n)]
if 2 not in li:
  print(-1)
else:
  ans = 0
  st = 0
  while st != 1:
    if (st == 0 and ans > 0) or ans > n:
      ans = -1
      break
    st = li[st]-1
    ans += 1
  print(ans)