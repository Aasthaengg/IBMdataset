a,b,c = map(int,input().split())
if a == b == c:
  if a%2 == b%2 == c%2 == 0:
    print(-1)
  else:
    print(0)
else:
  t = 0
  while t > -1:
    if a%2 == 1 or b%2 == 1 or c%2 == 1:
      break
    (a,b,c) = ((b+c)//2,(a+c)//2,(a+b)//2)
    t += 1
  print(t)
