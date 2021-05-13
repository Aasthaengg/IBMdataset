N,K=map(int,input().split())
if K%2==1:
  print((N//K)**3)
else:
  R=K//2
  print((N//K)**3+((N+R)//K)**3)