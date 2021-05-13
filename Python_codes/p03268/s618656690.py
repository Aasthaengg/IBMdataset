N,K = map(int,input().split())

if K%2 == 1:
  sur0 = []
  for i in range(1,N+1):
    if i%K == 0:
      sur0.append(i)
  print(len(sur0)**3)
    
else:
  sur0 = []
  surhalf = []
  for i in range(1,N+1):
    if i%K == 0:
      sur0.append(i)
    elif i%K == K/2:
      surhalf.append(i)
  print(len(sur0)**3 + len(surhalf)**3)