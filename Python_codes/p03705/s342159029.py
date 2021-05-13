n, a, b = map(int, input().split())
if n == 1:
  if a == b:
    print(1)
  else:
    print(0)
elif n == 2:
  if a > b:
    print(0)
  else:
    print(1)
else:
  ans = max(0, (n-2)*(b-a)+1)
  print(ans)