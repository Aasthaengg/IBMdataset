d, n = map(int, input().split())
if n < 100:
  ans = n * 100**d
  print(ans)
else:
  ans = 101 * 100**d
  print(ans)