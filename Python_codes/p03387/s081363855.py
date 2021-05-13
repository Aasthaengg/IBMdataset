ls = [int(i) for i in input().split()]
ls.sort()
ans = ls[2] - ls[1] + (ls[1] - ls[0] )// 2
if ((ls[2] - ls[1]) - (ls[2] - ls[0])) % 2 == 0:
  print(ans)
else:
  print(ans+2)