I = lambda: map(int, input().rstrip().split())
n = int(input())
if n <= 6:
  print(1)
else:
  ans = (n // 11) * 2
  if n % 11 == 0:
     pass
  elif (n // 11) % 2 == 0:
    if n % 11 <= 6:
      ans += 1
    else:
      ans += 2
  else:
    if n % 11 <= 5:
      ans += 1
    else:
      ans += 2
  print(ans)