a, b = map(int, input().split())
ans = a+b
if ans % 2:
  print("IMPOSSIBLE")
else:
  ans //= 2
  print(ans)