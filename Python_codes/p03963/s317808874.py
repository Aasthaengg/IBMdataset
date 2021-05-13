N,K  = map(int,input().split())
k = K-1
if N ==1:
  print(K)
  exit()
else:
  for i in range(N-1):
    K*=k
  
print(K)