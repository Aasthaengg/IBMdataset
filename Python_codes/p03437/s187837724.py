X,Y = list(map(int,input().split()))
if X % Y == 0:
  print(-1)
else:
  for i in range(1,1000000):
      if X*i > 10**18:
          print(-1)
          break
      if X*i % Y != 0:
          print(X*i)
          break