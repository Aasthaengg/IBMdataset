n,k = map(int,input().split())
now = (n-1) * (n-2) // 2 - k
if now < 0:
  print(-1)
else:
  print(n-1+now)
  for i in range(1,n):
    print(1,i+1)
  i = 1
  while True:
    if now > n-1-i:
      for j in range(i+1,n):
        print(i+1,j+1)
      now -= n-1-i
      i += 1
    else:
      for j in range(i+1,i+1+now):
        print(i+1,j+1)
      now -= now
      break