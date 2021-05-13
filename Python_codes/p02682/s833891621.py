# B Easy Linear Programming

a, b, c, k = map(int, input().split())

ans = 0
if k <= a:
  print(k)
else:
  ans += a
  if k-a <= b:
    print(ans)
  else:
    ans -= k-a-b
    print(ans)