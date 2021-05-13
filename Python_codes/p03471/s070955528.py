N, Y = map(int, input().split())

for i in range(0, N+1, 1):
  isFinish = False
  for j in range(0, N+1-i, 1):
    sen = 1000 * i
    gosen = 5000 * j
    man = 10000 * (N - i - j)
    
    if sen + gosen + man == Y:
      print(N - i - j, j, i)
      isFinish = True
      break
  
  if isFinish:
    break
else:
  print(-1, -1, -1)