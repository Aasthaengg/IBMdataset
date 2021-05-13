M,K=map(int,input().split())
if K>=2**M:
  print("-1")
elif M==1 and K==0:
  print("0 0 1 1")
elif M==1 and K==1:
  print("-1")
else:
  print(K)
  for i in range(K):
    print(i)
  for i in range(K+1,2**M):
    print(i)
  print(K)
  for i in range(2**M-1,K,-1):
    print(i)
  for i in range(K-1,-1,-1):
    print(i)
  
