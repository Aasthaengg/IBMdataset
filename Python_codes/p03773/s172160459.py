x, y = map(int, input().split())

ans = x + y

if ans > 23:
  print(ans%24)
else:
  print(ans)