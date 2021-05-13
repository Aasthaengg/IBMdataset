N,K=map(int,input().split())
if N==1:
  print(K)
else:
  for i in range(1,N):
    c=(K-1)**(i)
    
  print(K*c)