n, a, b = map(int, input().split())

if a % 2 == b % 2:
  print((b - a) // 2)
else:
  distA = a - 1
  distB = n - b
  if distA < distB:
    ans = distA + (b - distA - 1) // 2
    if b - distA % 2 == 1:
      print(ans)
    else:
      print(ans + 1)
  else:
    ans = distB + (n - (a + distB)) // 2
    if a + distB % 2 == n % 2:
      print(ans)
    else:
      print(ans + 1)
      
