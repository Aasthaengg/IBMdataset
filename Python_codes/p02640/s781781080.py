X, Y = map(int, input().split())

x = 0
while x<=X:
  if Y == x*2 + (X-x)*4:
    print('Yes')
    break
  x+=1
else:
  print('No')